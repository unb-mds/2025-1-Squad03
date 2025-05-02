import requests
from bs4 import BeautifulSoup
import json
import time
import os


def get_viewstate(soup):
    vs = soup.find('input', {'name': 'javax.faces.ViewState'})
    return vs['value'] if vs else None


def normalize(text):
    return ' '.join(text.strip().lower().split())


def scrape_estruturas():
    # Caminho absoluto para o arquivo JSON
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, '..', 'dados', 'cursos-de-graduacao.json')
    output_dir = os.path.join(script_dir, '..', 'dados', 'estruturas-curriculares')
    os.makedirs(output_dir, exist_ok=True)

    with open(json_path, 'r', encoding='utf-8') as f:
        cursos = json.load(f)

    # Filtrar apenas o curso desejado
    cursos = [c for c in cursos if normalize(c['nome']) == "ciência da computação"]

    base_url = "https://sigaa.unb.br/sigaa/public/curso/lista.jsf?nivel=G&aba=p-graduacao"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    session = requests.Session()
    session.headers.update(headers)

    # 1. Acessar página inicial para pegar cookies e viewstate
    resp = session.get(base_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    viewstate = get_viewstate(soup)

    for curso in cursos:
        nome_curso = curso['nome']
        print(f"Processando: {nome_curso}")

        # 2. Submeter formulário de busca
        form_data = {
            'form': 'form',
            'form:inputNome': nome_curso,
            'form:inputModalidade': 'Presencial',
            'form:j_id_jsp_1370969402_11': 'Buscar',
            'javax.faces.ViewState': viewstate
        }
        resp = session.post(base_url, data=form_data)
        soup = BeautifulSoup(resp.text, 'html.parser')
        viewstate = get_viewstate(soup)

        # Procurar na tabela de resultados pelo nome do curso
        tabela = soup.find('table', {'class': 'listagem'})
        if not tabela:
            print(f"Tabela de resultados não encontrada para: {nome_curso}")
            continue
        link = None
        for row in tabela.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) > 0:
                nome_tabela = normalize(cols[0].text)
                if normalize(nome_curso) in nome_tabela:
                    a = row.find('a', href=True)
                    if a and 'portal.jsf' in a['href']:
                        link = a['href']
                        break
        if not link:
            print(f"Não encontrado link da página do curso para: {nome_curso}")
            continue
        curso_url = f"https://sigaa.unb.br/sigaa/public/curso/{link}"

        # 4. Acessar página do curso
        resp = session.get(curso_url)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # Procurar o sub-menu 'Estruturas Curriculares' dentro da aba 'Ensino'
        estrutura_link = None
        # Procurar div do menu
        menu_ensino = soup.find('span', {'class': 'item-menu'}, string=lambda s: s and 'Ensino' in s)
        if menu_ensino:
            # Procurar o sub-menu logo após o span
            sub_menu = menu_ensino.find_parent('li')
            if sub_menu:
                for a in sub_menu.find_all('a', href=True):
                    if 'estruturaCurricular.jsf' in a['href'] or 'curriculo.jsf' in a['href']:
                        estrutura_link = a['href']
                        break
        # Fallback: procurar em toda a página
        if not estrutura_link:
            for a in soup.find_all('a', href=True):
                if 'estruturaCurricular.jsf' in a['href'] or 'curriculo.jsf' in a['href']:
                    estrutura_link = a['href']
                    break
        if not estrutura_link:
            print(f"Não encontrado link para estrutura curricular em: {curso_url}")
            continue
        if estrutura_link.startswith('/sigaa'):
            estrutura_url = f"https://sigaa.unb.br{estrutura_link}"
        elif estrutura_link.startswith('/'):
            estrutura_url = f"https://sigaa.unb.br/sigaa/public/curso{estrutura_link}"
        else:
            estrutura_url = f"https://sigaa.unb.br/sigaa/public/curso/{estrutura_link}"
        print(f"Link de estrutura curricular encontrado: {estrutura_url}")

        # 6. Acessar página de estruturas curriculares
        resp = session.get(estrutura_url)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # 7. Encontrar estrutura curricular mais recente com status 'Ativa'
        linhas = soup.find_all('tr')
        estrutura_ativa = None
        for tr in linhas:
            tds = tr.find_all('td')
            if len(tds) >= 2 and 'Ativa' in tds[1].text:
                estrutura_ativa = tr
                break
        if not estrutura_ativa:
            print(f"Não encontrada estrutura ativa para: {nome_curso}")
            continue

        # 8. Encontrar link do relatório (ícone do livro)
        relatorio_link = None
        for a in estrutura_ativa.find_all('a', href=True):
            if 'relatorioEstruturaCurricular.jsf' in a['href']:
                relatorio_link = a['href']
                break
        if not relatorio_link:
            print(f"Não encontrado link do relatório para: {nome_curso}")
            continue
        relatorio_url = f"https://sigaa.unb.br{relatorio_link}"

        # 9. Baixar conteúdo do relatório
        resp = session.get(relatorio_url)
        relatorio_html = resp.text
        output_path = os.path.join(output_dir, f"{nome_curso}.html")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(relatorio_html)
        print(f"Relatório salvo em: {output_path}")
        time.sleep(1)

        # Extrair estrutura curricular por nível
        extrair_estrutura_por_nivel(output_path, nome_curso, os.path.join(output_dir, f"{nome_curso}.json"))

    print("Scraping concluído!")


def extrair_estrutura_por_nivel(html_path, nome_curso, output_json):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    estrutura = {}
    nivel_atual = None

    for tag in soup.find_all(['b', 'tr']):
        # Detecta o início de um novo nível
        if tag.name == 'b' and 'Nível' in tag.text:
            nivel_atual = tag.text.strip()
            estrutura[nivel_atual] = []
        # Detecta optativas
        elif tag.name == 'b' and 'Optativas' in tag.text:
            nivel_atual = 'Optativas'
            estrutura[nivel_atual] = []
        # Detecta componentes curriculares
        elif tag.name == 'tr' and nivel_atual:
            tds = tag.find_all('td')
            if len(tds) >= 2:
                # Exemplo: CIC0003 - INTRODUÇÃO AOS SISTEMAS COMPUTACIONAIS - 60h
                dados = tds[0].text.strip().split(' - ')
                if len(dados) >= 3:
                    codigo = dados[0]
                    nome = ' - '.join(dados[1:-1])
                    carga = dados[-1]
                    natureza = tds[1].text.strip()
                    estrutura[nivel_atual].append({
                        'codigo': codigo,
                        'nome': nome,
                        'carga_horaria': carga,
                        'natureza': natureza
                    })

    # Salvar em JSON
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump({
            'curso': nome_curso,
            'estrutura': estrutura
        }, f, ensure_ascii=False, indent=2)
    print(f"Estrutura curricular salva em: {output_json}")


if __name__ == "__main__":
    scrape_estruturas()