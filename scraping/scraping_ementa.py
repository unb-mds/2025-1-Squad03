import requests
from bs4 import BeautifulSoup
import json
import time
import pandas as pd
from urllib.parse import urljoin

def scrape_cursos():
    # URL base
    base_url = "https://sigaa.unb.br/sigaa/public/curso/lista.jsf?nivel=G&aba=p-graduacao"
    
    # Carregar cursos do JSON
    with open('dados/cursos-de-graduacao.json', 'r', encoding='utf-8') as f:
        cursos = json.load(f)
    
    # Criar lista para armazenar resultados
    resultados = []
    
    # Iniciar sessão
    session = requests.Session()
    
    # Fazer requisição inicial para obter cookies
    response = session.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extrair viewstate
    viewstate = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
    
    # Para cada curso
    for curso in cursos:
        nome_curso = curso['nome']
        print(f"Processando curso: {nome_curso}")
        
        # Preparar dados do formulário
        form_data = {
            'form': 'form',
            'form:inputNome': nome_curso,
            'form:inputModalidade': '',
            'form:j_id_jsp_1370969402_11': 'Buscar',
            'javax.faces.ViewState': viewstate
        }
        
        # Enviar requisição de busca
        response = session.post(base_url, data=form_data)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Atualizar viewstate
        viewstate = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        
        # Procurar por cursos com ementa ATIVA
        tabela = soup.find('table', {'class': 'listagem'})
        if tabela:
            linhas = tabela.find_all('tr')
            for linha in linhas:
                if 'ATIVA' in linha.text:
                    # Extrair informações
                    colunas = linha.find_all('td')
                    if len(colunas) >= 6:
                        info_curso = {
                            'nome': nome_curso,
                            'grau': colunas[1].text.strip(),
                            'turno': colunas[2].text.strip(),
                            'sede': colunas[3].text.strip(),
                            'modalidade': colunas[4].text.strip(),
                            'coordenador': colunas[5].text.strip(),
                            'situacao': 'ATIVA'
                        }
                        resultados.append(info_curso)
        
        # Esperar um pouco para não sobrecarregar o servidor
        time.sleep(1)
    
    # Converter resultados para DataFrame
    df = pd.DataFrame(resultados)
    
    # Salvar resultados
    df.to_csv('dados/cursos_ativos.csv', index=False, encoding='utf-8-sig')
    print("Scraping concluído! Resultados salvos em 'dados/cursos_ativos.csv'")

if __name__ == "__main__":
    scrape_cursos()