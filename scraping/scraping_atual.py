import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from urllib.parse import urljoin
import os
import re
'''
o arquivo 'scraping_atual.py', é uma arquivo baseado no 'scraping.py', porém, adequado às
necessidades do projeto. O scraping das disciplinas deverao ser feitos por este arquivo
que está sendo lido no momento de agora.
'''

def coleta_dados(session, component_id, viewstate, base_url, params, debug=False):
    """
    Função para obter os detalhes de um componente curricular
    acessando a página de detalhes do componente

    Args:
        session: Sessão HTTP
        component_id: ID do componente curricular
        viewstate: ViewState para o formulário JSF
        base_url: URL base do SIGAA
        debug: Se True, salva a resposta HTML em um arquivo para debug

    Returns:
        Dicionário com os detalhes do componente curricular
    """
    print(
        f"[{time.strftime('%H:%M:%S')}] Acessando detalhes do componente ID: {component_id}..."
    )

    # A URL é a mesma da página principal, pois o site usa JavaScript para fazer a requisição AJAX
    details_url = base_url
    response = session.get(details_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #view_state = soup.find('input', {'name': 'javax.faces.ViewState'})['value']

    # Preparar dados para requisição POST baseado no que vemos no onclick do link
    form_data = {
        "javax.faces.ViewState": viewstate,
        "formTurma": "formTurma"
        #"formTurma:aqui": "formTurma:aqui",
        #"id": component_id
        #"publico": "public",
    
    }
    form_data.update(params)

    print(soup.find('input', {'name': 'javax.faces.ViewState'})['value'])
    #return 0

    try:
        # Enviar requisição para obter os detalhes do componente
        print(
            f"[{time.strftime('%H:%M:%S')}] Enviando POST para obter detalhes do componente..."
        )
        
        response = session.post(details_url, data=form_data,  
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': details_url
            })

        # Salvar a resposta para debug somente se o flag debug estiver ativo
        if debug:
            with open(
                f"componente_{component_id}_response.html", "w", encoding="utf-8"
            ) as f:
                f.write(response.text)

        
        if response.status_code != 200:
            print(
                f"[{time.strftime('%H:%M:%S')}] ERRO ao acessar detalhes do componente: Status {response.status_code}"
            )
            return {}

        # Parsear o HTML da página de detalhes
        print(response)
        details_soup = BeautifulSoup(response.text, "html.parser")
        #viewstate = details_soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        #form_data['javax.faces.ViewState'] = viewstate

        # Verificar se o HTML foi carregado corretamente
        if not details_soup or not details_soup.find_all():
            print(
                f"[{time.strftime('%H:%M:%S')}] ERRO: Não foi possível carregar o HTML da página de detalhes do componente."
            )
            return {}

        # Inicializar dicionário para armazenar os dados extraídos
        details = {}
        ementa = ""

        # Procurar tabela principal com as informações do componente
        dados_gerais_table = details_soup.find("table", {"class": "visualizacao"})
        #print(dados_gerais_table)
        #return(0)
        if dados_gerais_table:
            print('passou')
            print(f"[{time.strftime('%H:%M:%S')}] Tabela de dados gerais encontrada.")
            
            # Extrair dados estruturados
            rows = dados_gerais_table.find_all("tr")
            for row in rows:
                cells = row.find_all(["th", "td"])
                if len(cells) >= 2:
                    label = cells[0].text.strip().rstrip(':')
                    value = cells[1].text.strip()
                    details[label] = value

                    # Extrair equivalências como lista de códigos, note que algumas alterações foram feitas
                    #em relação ao original
                    if "Equivalências" in label and "Histórico de Equivalências" not in label:

                        equivalencias = []
                        for ac in cells[1].find_all("acronym"):
                            codigo = ac.get_text(strip=True)
                            print(f'variavel código = {codigo}')
                            descricao = ac.get("title", "").split(" - ")[-1]
                            print(f'variavel descricao = {descricao}')
                            equivalencias.append(f"{codigo} ({descricao})")
                        details["Equivalências"] = ", ".join(equivalencias) if equivalencias else "Nenhuma"
                        print(f'lista equivalencias = {equivalencias}')
                        print(details["Equivalências"])

                    # Capturar ementa
                    #if "Ementa" in label or "Descrição" in label:
                        #ementa = value

        # Se não encontrou a tabela principal, tentar métodos alternativos
        if not details:
            print(
                f"[{time.strftime('%H:%M:%S')}] Tentando métodos alternativos para encontrar dados..."
            )

            # Método alternativo: procurar por todas as tabelas
            tables = details_soup.find_all("table")
            #print("passou aqui")
            #print(tables)
            for table in tables:
                # Verificar se é a tabela de dados gerais
                header = table.find("tr", {"class": "linhaTitulo"})
                if header and "Dados Gerais do Componente Curricular" in header.text:
                    print("passou aqui")
                    rows = table.find_all("tr")
                    for row in rows:
                        cells = row.find_all(["th", "td"])
                        if len(cells) >= 2:
                            label = cells[0].text.strip()
                            if label.endswith(":"):
                                label = label[:-1]
                            value = cells[1].text.strip()
                            details[label] = value

                            # Verificar se é a ementa
                            if "Ementa" in label or "Descrição" in label:
                                ementa = value
                    

        # Extrair campos específicos e montar o dicionário de retorno
        component_details = {
            "tipo_componente": details.get(
                "Tipo do Componente Curricular", "Não informado"
            ),
            "modalidade_educacao": details.get(
                "Modalidade de Educação", "Não informado"
            ),
            "unidade_responsavel": details.get("Unidade Responsável", "Não informado"),
            "codigo_componente": details.get("Código", "Não informado"),
            "nome_componente": details.get("Nome", "Não informado"),
            "pre_requisitos": details.get("Pré-Requisitos", "Não informado"),
            "co_requisitos": details.get("Co-Requisitos", "Não informado"),
            "equivalencias": details.get("Equivalências", "Não informado"),
            "excluir_avaliacao": details.get(
                "Excluir da Avaliação Institucional", "Não informado"
            ),
            "matriculavel_online": details.get("Matriculável On-Line", "Não informado"),
            "horario_flexivel": details.get(
                "Horário Flexível da Turma", "Não informado"
            ),
            "permite_multiplas_aprovacoes": details.get(
                "Permite Múltiplas Aprovações", "Não informado"
            ),
            "quantidade_avaliacoes": details.get(
                "Quantidade de Avaliações", "Não informado"
            ),
            "ementa": ementa or details.get("Ementa/Descrição", "Não informado"),
            "carga_horaria_total": details.get(
                "Total de Carga Horária do Componente", "Não informado"
            ),
        }

        print(
            f"[{time.strftime('%H:%M:%S')}] Detalhes do componente {component_id} extraídos com sucesso!"
        )
        return component_details

    except Exception as e:
        print(
            f"[{time.strftime('%H:%M:%S')}] ERRO ao processar detalhes do componente: {str(e)}"
        )
        import traceback

        traceback.print_exc()
        return {}


def scrape_unb_classes(id_depto, debug=False):
    """
    Função para fazer scraping das turmas da UnB no SIGAA,
    preenchendo automaticamente o formulário com os campos:
    - Nível de Ensino: GRADUAÇÃO (valor "G")
    - Unidade: CAMPUS UNB GAMA: FACULDADE DE CIÊNCIAS E TECNOLOGIAS EM ENGENHARIA - BRASÍLIA (valor "673")
    - Ano-Período: 2025-1

    Args:
        debug: Se True, salva as respostas HTML em arquivos para debug
    """
    # Inicializa a lista de turmas aqui, fora do loop
    turmas_data = []
    
    count = 0
    for id_atual in id_depto:
        if count<3:
            count+=1
            print("\n====== INICIANDO SCRAPING DAS TURMAS DA UNB ======")
            print(f"[{time.strftime('%H:%M:%S')}] Processo iniciado para departamento ID: {id_atual}")

            # URL base do sistema SIGAA
            base_url = "https://sigaa.unb.br/sigaa/public/turmas/listar.jsf"

            # Fazendo a primeira requisição para obter os cookies e tokens
            session = requests.Session()

            try:
                print(f"[{time.strftime('%H:%M:%S')}] Enviando requisição GET inicial...")
                response = session.get(base_url, timeout=30)
                if response.status_code != 200:
                    print(
                        f"[{time.strftime('%H:%M:%S')}] ERRO: Status da resposta: {response.status_code}"
                    )
                    continue  # Vai para o próximo departamento em vez de retornar
            except requests.exceptions.RequestException as e:
                print(f"[{time.strftime('%H:%M:%S')}] ERRO ao acessar o site: {str(e)}")
                continue  # Vai para o próximo departamento

            # Parsear o HTML da página
            soup = BeautifulSoup(response.text, "html.parser")

            # Extrair o viewstate (necessário para o formulário)
            print(f"[{time.strftime('%H:%M:%S')}] Buscando ViewState no formulário...")
            viewstate_element = soup.find("input", {"name": "javax.faces.ViewState"})

            if not viewstate_element:
                print(f"[{time.strftime('%H:%M:%S')}] ERRO: ViewState não encontrado.")
                continue  # Vai para o próximo departamento

            viewstate = viewstate_element["value"]

            # Identificar o ID do formulário e dos campos
            form = soup.find("form", {"id": "formTurma"})
            if not form:
                print(f"[{time.strftime('%H:%M:%S')}] ERRO: Formulário não encontrado.")
                continue

            # Obter o ID do botão de busca
            buscar_button = form.find("input", {"value": "Buscar"})
            if not buscar_button:
                print(f"[{time.strftime('%H:%M:%S')}] ERRO: Botão de busca não encontrado.")
                continue

            buscar_id = buscar_button.get("id", "formTurma:j_id_jsp_1370969402_11")

            # Preparar os dados do formulário com os valores exatos
            form_data = {
                "formTurma": "formTurma",
                "formTurma:inputNivel": "G",
                "formTurma:inputDepto": id_atual,
                "formTurma:inputAno": "2025",
                "formTurma:inputPeriodo": "1",
                buscar_id: "Buscar",
                "javax.faces.ViewState": viewstate,
            }

            # Realizar a busca (enviar o formulário)
            print(f"[{time.strftime('%H:%M:%S')}] ENVIANDO FORMULÁRIO DE BUSCA...")
            try:
                search_response = session.post(base_url, data=form_data, timeout=60)
                if search_response.status_code != 200:
                    print(
                        f"[{time.strftime('%H:%M:%S')}] ERRO: Status da resposta POST: {search_response.status_code}"
                    )
                    continue
            except requests.exceptions.RequestException as e:
                print(f"[{time.strftime('%H:%M:%S')}] ERRO ao enviar o formulário: {str(e)}")
                continue

            # Parsear os resultados
            results_soup = BeautifulSoup(search_response.text, "html.parser")

            # Verificar se existem resultados
            if "Nenhuma turma encontrada" in search_response.text:
                print(
                    f"[{time.strftime('%H:%M:%S')}] AVISO: Nenhuma turma encontrada para departamento {id_atual}."
                )
                continue

            # Extrair tabela de resultados
            tables = results_soup.find_all("table", {"class": "listagem"})

            if not tables:
                print(
                    f"[{time.strftime('%H:%M:%S')}] ERRO: Tabela de resultados não encontrada para departamento {id_atual}."
                )
                continue

            # Processar os dados da tabela
            for table_counter, table in enumerate(tables, 1):
                # Variáveis para armazenar os detalhes do componente atual
                current_component_id = None
                current_component_details = {}
                current_component_name = ""

                rows = table.find_all("tr")
                
                # Processar as linhas da tabela
                for row in rows:
                    # Verificar se é uma linha de agrupador
                    if "agrupador" in row.get("class", []):
                        link = row.find("a")
                        if link:
                            onclick = link.get("onclick", "")
                            id_match = re.search(r"'id':'(\d+)'", onclick)
                            params = re.search(r"\{([^}]+)\}", onclick).group(1)
                            params_dict = dict(re.findall(r"'([^']+)'\s*:\s*'([^']+)'", params))

                            if id_match:
                                current_component_id = id_match.group(1)
                                title_span = link.find("span", {"class": "tituloDisciplina"})
                                if title_span:
                                    current_component_name = title_span.text.strip()

                                print(
                                    f"[{time.strftime('%H:%M:%S')}] Encontrado componente: {current_component_name} (ID: {current_component_id})"
                                )

                                time.sleep(1)

                                viewstate = results_soup.find('input', {'name': 'javax.faces.ViewState'})['value']
                                current_component_details = coleta_dados(
                                    session, current_component_id, viewstate, base_url, params_dict, debug
                                )

                    # Processar linhas de dados
                    elif "linhaTitulo" not in row.get("class", []) and "agrupador" not in row.get("class", []):
                        cols = row.find_all("td")

                        if len(cols) >= 5:
                            try:
                                turma_info = {
                                    "codigo": cols[0].text.strip(),
                                    "disciplina": current_component_name or cols[1].text.strip(),
                                    "turma": cols[2].text.strip(),
                                    "horario": cols[3].text.strip(),
                                    "local": cols[4].text.strip(),
                                    "docente": cols[5].text.strip() if len(cols) > 5 else "Não informado",
                                    "departamento_id": id_atual  # Adicionando o ID do departamento para referência
                                }

                                if current_component_details:
                                    turma_info.update(current_component_details)

                                turmas_data.append(turma_info)
                            except Exception as e:
                                print(
                                    f"[{time.strftime('%H:%M:%S')}] ERRO ao processar uma linha: {str(e)}"
                                )

    # Criar DataFrame com todos os resultados após processar todos os departamentos
    if not turmas_data:
        print(f"[{time.strftime('%H:%M:%S')}] Nenhum dado encontrado para nenhum departamento.")
        return None

    df_turmas = pd.DataFrame(turmas_data)

    print(
        f"[{time.strftime('%H:%M:%S')}] Extração concluída. Foram encontradas {len(df_turmas)} turmas no total."
    )

    # Criar pasta de dados se não existir
    data_dir = "dados"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Salvar em CSV
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    csv_filename = os.path.join(data_dir, f"turmas_unb_gama_{timestamp}.csv")
    print(f"[{time.strftime('%H:%M:%S')}] Salvando dados em: {csv_filename}")

    try:
        df_turmas.to_csv(csv_filename, index=False, encoding="utf-8-sig")
        print(f"[{time.strftime('%H:%M:%S')}] Dados salvos com sucesso.")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] ERRO ao salvar CSV: {str(e)}")

    print(f"[{time.strftime('%H:%M:%S')}] ====== PROCESSO CONCLUÍDO COM SUCESSO ======")
    return df_turmas


if __name__ == "__main__":
    try:
        # Por padrão, executar sem debug
        debug_mode = False

        # Verificar se há argumentos de linha de comando
        import sys

        if len(sys.argv) > 1 and sys.argv[1].lower() == "--debug":
            debug_mode = True
            print(
                f"[{time.strftime('%H:%M:%S')}] Modo de depuração ativado. Os arquivos HTML serão salvos."
            )
        '''
        armazenando os ID dos departamentos em uma lista, percebe-se que os ID ja estao armazenados
        no arquivo csv 'departamentos_unb_2.csv'
        '''

        import csv
        csv_path = 'dados/departamentos_unb_2.csv'
        count = 0
        with open(csv_path,'r') as file:
            csv_reader = csv.reader(file)
            data_lista = []
            for row in csv_reader:
                #x = row
                count +=1
                if (row[0]=='ï»¿id'):
                    print('excessao')

                elif (int(row[0])==0):
                    print('excessao')

                
                else:
                    data_lista.append(int(row[0]))


        resultado = scrape_unb_classes(data_lista,debug=debug_mode)
        if resultado is not None:
            print(
                f"[{time.strftime('%H:%M:%S')}] Primeiras linhas dos dados extraídos:"
            )
            print(resultado.head())
        else:
            print(f"[{time.strftime('%H:%M:%S')}] Nenhum resultado foi retornado.")
    except Exception as e:
        print(
            f"[{time.strftime('%H:%M:%S')}] ERRO CRÍTICO durante o scraping: {str(e)}"
        )
        import traceback

        traceback.print_exc()
