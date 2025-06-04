# Contents of your testeCode.py file (no changes needed within the function itself for this error)
import json
import re

def process_retrieval_results(retrieval_results_list_of_dicts):
    """
    Processa os resultados brutos de recuperação do RAGFlow, que vêm como uma lista de dicionários.
    Cada dicionário contém a chave 'content' com a string da disciplina pré-processada.
    Agrupa disciplinas, consolida ementas e desduplica.

    Args:
        retrieval_results_list_of_dicts (list): A lista de dicionários que o nó Retrieval retorna.
                                                Ex: [{"chunks": "[{...}]", "content": "...", "similarity": ...}, ...]

    Returns:
        str: Uma string JSON contendo a lista das 4 melhores disciplinas únicas e consolidadas.
             Retorna uma string '[]' se nenhum resultado for encontrado ou válido.
    """
    
    # Esta parte permanece como estava no último ajuste, para lidar com o tipo de entrada
    if not isinstance(retrieval_results_list_of_dicts, list):
        try:
            # This will correctly use the imported 'json' module
            retrieval_output_list = json.loads(retrieval_results_list_of_dicts)
        except json.JSONDecodeError:
            return json.dumps([]) # Uses 'json' module
    else:
        retrieval_output_list = retrieval_results_list_of_dicts


    if not retrieval_output_list:
        return json.dumps([]) # Uses 'json' module

    consolidated_disciplines = {}
    ordered_unique_keys = [] 

    def parse_discipline_string(discipline_string):
        parsed_data = {
            "Disciplina": "",
            "Unidade responsavel": "",
            "Ementa": ""
        }
        
        cleaned_string = re.sub(r'Document:.*?Relevant fragments as following:---\nID: \d+\n?', '', discipline_string, flags=re.DOTALL).strip()
        cleaned_string = cleaned_string.replace('\r', ' ').replace('\n', ' ').strip()
        
        fields = cleaned_string.split('; ')
        
        for field in fields:
            if field.startswith("Disciplina:"):
                parsed_data["Disciplina"] = field.replace("Disciplina:", "").strip()
            elif field.startswith("Unidade responsavel:"):
                parsed_data["Unidade responsavel"] = field.replace("Unidade responsavel:", "").strip()
            elif field.startswith("Ementa:"):
                ementa_content = field.replace("Ementa:", "").strip()
                parsed_data["Ementa"] = ementa_content
        
        return parsed_data

    for retrieval_item_dict in retrieval_output_list:
        raw_discipline_string = None
        if "content" in retrieval_item_dict and isinstance(retrieval_item_dict["content"], str):
            raw_discipline_string = retrieval_item_dict["content"]
            
        elif "chunks" in retrieval_item_dict and isinstance(retrieval_item_dict["chunks"], str):
            try:
                # This will correctly use the imported 'json' module
                chunks_list_inner = json.loads(retrieval_item_dict["chunks"])
                if chunks_list_inner and isinstance(chunks_list_inner, list):
                    raw_discipline_string = chunks_list_inner[0].get("content_with_weight", "")
            except json.JSONDecodeError:
                pass

        if not raw_discipline_string:
            continue

        parsed_discipline_data = parse_discipline_string(raw_discipline_string)
        
        disc_name_full = parsed_discipline_data.get("Disciplina")
        
        unique_key = disc_name_full 
        if not unique_key: 
            continue

        if unique_key not in consolidated_disciplines:
            ordered_unique_keys.append(unique_key)
            
            consolidated_disciplines[unique_key] = {
                "Disciplina": disc_name_full,
                "Unidade responsavel": parsed_discipline_data.get("Unidade responsavel", "Não disponível"),
                "Ementa": parsed_discipline_data.get("Ementa", "")
            }
        else:
            new_ementa_part = parsed_discipline_data.get("Ementa", "").strip()
            current_ementa = consolidated_disciplines[unique_key]["Ementa"]
            
            if new_ementa_part and new_ementa_part not in current_ementa:
                if current_ementa.strip() and not current_ementa.strip().endswith('.') and not current_ementa.strip().endswith(';'):
                    consolidated_disciplines[unique_key]["Ementa"] += ". " + new_ementa_part
                elif current_ementa.strip():
                    consolidated_disciplines[unique_key]["Ementa"] += " " + new_ementa_part
                else:
                    consolidated_disciplines[unique_key]["Ementa"] = new_ementa_part
            
            if not consolidated_disciplines[unique_key]["Unidade responsavel"] or consolidated_disciplines[unique_key]["Unidade responsavel"] == "Não disponível":
                if parsed_discipline_data.get("Unidade responsavel") and parsed_discipline_data.get("Unidade responsavel") != "Não disponível":
                    consolidated_disciplines[unique_key]["Unidade responsavel"] = parsed_discipline_data.get("Unidade responsavel")

    final_results = []
    for key in ordered_unique_keys:
        final_results.append(consolidated_disciplines[key])
        if len(final_results) >= 4:
            break
            
    # This will correctly use the imported 'json' module,
    # as long as the global 'json' name (if this script is run directly with the test data below)
    # is not shadowing the module at the time of this function's execution.
    return json.dumps(final_results)

# ---- How to run your test ----
# Save the above code as testeCode.py

# Then, in a separate script or Python console:
# from testeCode import process_retrieval_results
# import json # Import the json module, it's fine here if not shadowed later

# RENAME your data variable to avoid conflict with the json module
input_data_list = [
  {
    "chunks": "[{\"chunk_id\": \"7dcbe123d9e39ffc\", \"content_ltks\": \"disciplina introducao a inteligencia artifici unidad responsavel depto ciencia da computacao ementa introducao a historico e conceito deia agent inteligent resolucao de problema por metodo de busca conhecimento e raciocinio logico representacao de conhecimento em logica de primeira ordem regra de producao noco de logica difusa construcao de sistema baseado em conhecimento noco de incerteza aprendizagem de maquina modelo supervisionado e nao supervisionado aplicaco deia\", \"content_with_weight\": \"\\rDisciplina:INTRODUCAO A INTELIGENCIA ARTIFICIAL; Unidade responsavel: DEPTO CIENCIAS DA COMPUTACAO; Ementa: Introducao a historico e conceitos de IA. Agentes Inteligentes. Resolucao de; problemas por Metodos de Busca. Conhecimento e Raciocinio Logico.; Representacao de Conhecimento em Logica de Primeira Ordem. Regras de; Producao. Nocoes de Logica Difusa. Construcao de Sistemas Baseados em; Conhecimento. Nocoes de Incerteza. Aprendizagem de Maquinas. Modelos; Supervisionados e Nao Supervisionados. Aplicacoes de IA.\\r\", \"doc_id\": \"a10335c6417711f0baa41a352721c2dd\", \"docnm_kwd\": \"preprocessed_turmas_depto_508.txt\", \"kb_id\": \"4cf3205640df11f0ad49a2f043f8e120\", \"important_kwd\": [], \"image_id\": \"\", \"similarity\": 0.5443228698765386, \"vector_similarity\": 0.4199617683618644, \"term_similarity\": 0.6460728620249083, \"vector\": []}]", # Vector data omitted for brevity
    "content": "\nDocument: preprocessed_turmas_depto_508.txt \nRelevant fragments as following:\n---\nID: 0\n\rDisciplina:INTRODUCAO A INTELIGENCIA ARTIFICIAL; Unidade responsavel: DEPTO CIENCIAS DA COMPUTACAO; Ementa: Introducao a historico e conceitos de IA. Agentes Inteligentes. Resolucao de; problemas por Metodos de Busca. Conhecimento e Raciocinio Logico.; Representacao de Conhecimento em Logica de Primeira Ordem. Regras de; Producao. Nocoes de Logica Difusa. Construcao de Sistemas Baseados em; Conhecimento. Nocoes de Incerteza. Aprendizagem de Maquinas. Modelos; Supervisionados e Nao Supervisionados. Aplicacoes de IA.\r\n"
  },
  {
    "chunks": "[{\"chunk_id\": \"7dcbe123d9e39ffc\", \"content_ltks\": \"disciplina introducao a inteligencia artifici unidad responsavel depto ciencia da computacao ementa introducao a historico e conceito deia agent inteligent resolucao de problema por metodo de busca conhecimento e raciocinio logico representacao de conhecimento em logica de primeira ordem regra de producao noco de logica difusa construcao de sistema baseado em conhecimento noco de incerteza aprendizagem de maquina modelo supervisionado e nao supervisionado aplicaco deia\", \"content_with_weight\": \"\\rDisciplina:INTRODUCAO A INTELIGENCIA ARTIFICIAL; Unidade responsavel: DEPTO CIENCIAS DA COMPUTACAO; Ementa: Introducao a historico e conceitos de IA. Agentes Inteligentes. Resolucao de; problemas por Metodos de Busca. Conhecimento e Raciocinio Logico.; Representacao de Conhecimento em Logica de Primeira Ordem. Regras de; Producao. Nocoes de Logica Difusa. Construcao de Sistemas Baseados em; Conhecimento. Nocoes de Incerteza. Aprendizagem de Maquinas. Modelos; Supervisionados e Nao Supervisionados. Aplicacoes de IA.\\r\", \"doc_id\": \"a10335c6417711f0baa41a352721c2dd\", \"docnm_kwd\": \"preprocessed_turmas_depto_508.txt\", \"kb_id\": \"4cf3205640df11f0ad49a2f043f8e120\", \"important_kwd\": [], \"image_id\": \"\", \"similarity\": 0.5443228698765386, \"vector_similarity\": 0.4199617683618644, \"term_similarity\": 0.6460728620249083, \"vector\": []}]" # Vector data omitted for brevity
    # No "content" field in this item from your original data, so it will use "chunks"
  },
  {
    "chunks": "[{\"chunk_id\": \"76bc99e305624195\", \"content_ltks\": \"disciplina fundamento logico de inteligencia artifici unidad responsavel campu unb gama faculdad de ciencia e tecnologia em engenharia ementa introducao a logica classica logica de primeira ordem representaco proposicionai procedimento automatico de prova problema de satisfatibilidad sat algoritmo para sat busca em grafo forma nao clausai de representacao planejamento automatizado aplicaco em planejamento automatizado\", \"content_with_weight\": \"Disciplina:FUNDAMENTOS LOGICOS DE INTELIGENCIA ARTIFICIAL; Unidade responsavel: CAMPUS UNB GAMA: FACULDADE DE CIENCIAS E TECNOLOGIAS EM ENGENHARIA; Ementa: Introducao a logica classica;; Logica de primeira ordem;; Representacoes proposicionais;; Procedimentos automaticos de prova;; Problema de satisfatibilidade (SAT);; Algoritmos para SAT;; Busca em grafos;; Formas nao clausais de representacao;; Planejamento automatizado;; Aplicacoes em planejamento automatizado.\\r\", \"doc_id\": \"a18d8618417711f094d61a352721c2dd\", \"docnm_kwd\": \"preprocessed_turmas_depto_673.txt\", \"kb_id\": \"4cf3205640df11f0ad49a2f043f8e120\", \"important_kwd\": [], \"image_id\": \"\", \"similarity\": 0.5442092928582574, \"vector_similarity\": 0.41970937498790606, \"term_similarity\": 0.6460728620249083, \"vector\": []}]" # Vector data omitted
  },
  {
    "chunks": "[{\"chunk_id\": \"acb9bbaae0fd01d1\", \"content_ltks\": \"disciplina noco de inteligencia artifici unidad responsavel depto engenharia eletrica ementa 1 introducao historico e denominaco aprendizado rede neurai problema de interess 2 aprendizado supervisionado regressao linear descida por gradient regressao logistica funco de custo criterio de perform entropia cruzada vizinho mai proximo 3 aprendizado nao supervisionado agrupamento reducao de dimensionalidad amostragem de gibb 4 rede neurai artificiai perceptron perceptron multicamada funco de ativacao regularizacao 5 deep learn rede convolucionai autocodificador introducao a rede recorrent 6 outra tecnica algoritmo genetico logica fuzzi 7 questo etica sociai ede seguranca vie privacidad seguranca impacto sociai\", \"content_with_weight\": \"\\rDisciplina:NOCOES DE INTELIGENCIA ARTIFICIAL; Unidade responsavel: DEPTO ENGENHARIA ELETRICA; Ementa: 1. Introducao; Historico e Denominacoes; Aprendizado; Redes Neurais; Problemas de interesse.; 2. Aprendizado Supervisionado; Regressao linear; Descida por gradiente; Regressao logistica; Funcoes de custo; Criterios de performance; Entropia cruzada; Vizinhos mais proximos.; 3. Aprendizado Nao-supervisionado; Agrupamento; Reducao de dimensionalidade; Amostragem de Gibbs.; 4. Redes Neurais Artificiais; Perceptron; Perceptron multicamada; Funcoes de Ativacao; Regularizacao.; 5. \\\"Deep Learning\\\"; Redes convolucionais; Autocodificadores; Introducao as redes recorrentes.; 6. Outras tecnicas; Algoritmos Geneticos; Logica \\\"fuzzy\\\".; 7. Questoes Eticas, Sociais e de Seguranca; Vies; Privacidade; Seguranca; Impactos sociais\\r\", \"doc_id\": \"a0c6500c417711f082441a352721c2dd\", \"docnm_kwd\": \"preprocessed_turmas_depto_443.txt\", \"kb_id\": \"4cf3205640df11f0ad49a2f043f8e120\", \"important_kwd\": [], \"image_id\": \"\", \"similarity\": 0.5409206542055139, \"vector_similarity\": 0.41240128909292073, \"term_similarity\": 0.6460728620249083, \"vector\": []}]" # Vector data omitted
  },
  {
    "chunks": "[{\"chunk_id\": \"45ace448b8503441\", \"content_ltks\": \"disciplina inteligencia artifici unidad responsavel campu unb gama faculdad de ciencia e tecnologia em engenharia ementa descricao o estado da artemia engenharia do conhecimento ontologia arquitetura de sistema baseado em conhecimento metodologia para desenvolvimento de sistema inteligent paradigma simbolico conexionista evolucionario e hibrido outro assunto relevant dependendo o periodo e ano aser ministrada esta disciplina aplicaco projeto\", \"content_with_weight\": \"\\rDisciplina:INTELIGENCIA ARTIFICIAL; Unidade responsavel: CAMPUS UNB GAMA: FACULDADE DE CIENCIAS E TECNOLOGIAS EM ENGENHARIA; Ementa: DESCRICAO:O estado da arte em IA. Engenharia do conhecimento. Ontologias. Arquiteturas de sistemas baseados em conhecimento. Metodologias para desenvolvimento de sistemas inteligentes. Paradigmas simbolico, conexionista, evolucionario e hibrido. Outros assuntos relevantes dependendo o periodo e ano a ser ministrada esta disciplina. Aplicacoes. Projeto.\\r\", \"doc_id\": \"a18d8618417711f094d61a352721c2dd\", \"docnm_kwd\": \"preprocessed_turmas_depto_673.txt\", \"kb_id\": \"4cf3205640df11f0ad49a2f043f8e120\", \"important_kwd\": [], \"image_id\": \"\", \"similarity\": 0.533030616954558, \"vector_similarity\": 0.39486787297968534, \"term_similarity\": 0.6460728620249083, \"vector\": []}]" # Vector data omitted
  },
  {
    "chunks": "[{\"chunk_id\": \"6ae249e10a6e4a78\", \"content_ltks\": \"disciplina biologia quantitativa unidad responsavel instituto de ciencia biologica ementa apresentacao de fundamento teorico ede exercicio pratico sobr metodo quantitativo usado em biologia na area de ciencia de dado biologia de campo bioestatistica comr e python geoprocessamento e biologia da paisagem com softwar livr e tecnica de inteligencia artifici com rede neurai algoritmo genetico e automato celular\", \"content_with_weight\": \"\\rDisciplina:BIOLOGIA QUANTITATIVA; Unidade responsavel: INSTITUTO DE CIENCIAS BIOLOGICAS; Ementa: Apresentacao de fundamentos teoricos e de exercicios praticos sobre metodos; quantitativos usados em biologia, nas areas de ciencia de dados, biologia de campo,; bioestatistica com R e Python, geoprocessamento e biologia da paisagem com; softwares livres, e tecnicas de inteligencia artificial com redes neurais, algoritmos; geneticos e automatos celulares.\", \"doc_id\": \"a0cf14f8417711f082441a352721c2dd\", \"docnm_kwd\": \"preprocessed_turmas_depto_455.txt\", \"kb_id\": \"4cf3205640df11f0ad49a2f043f8e120\", \"important_kwd\": [], \"image_id\": \"\", \"similarity\": 0.5202456756235558, \"vector_similarity\": 0.3664568922441251, \"term_similarity\": 0.6460728620249083, \"vector\": []}]" # Vector data omitted
  }
]

# Now call the function with the renamed data variable
# The 'json' module will be correctly used by json.dumps() inside the function.
output_json_string = process_retrieval_results(input_data_list)
print(output_json_string)

# Expected output (structure and first few items based on your data, formatting may vary slightly):
# [{"Disciplina": "INTRODUCAO A INTELIGENCIA ARTIFICIAL", "Unidade responsavel": "DEPTO CIENCIAS DA COMPUTACAO", "Ementa": "Introducao a historico e conceitos de IA. Agentes Inteligentes. Resolucao de; problemas por Metodos de Busca. Conhecimento e Raciocinio Logico.; Representacao de Conhecimento em Logica de Primeira Ordem. Regras de; Producao. Nocoes de Logica Difusa. Construcao de Sistemas Baseados em; Conhecimento. Nocoes de Incerteza. Aprendizagem de Maquinas. Modelos; Supervisionados e Nao Supervisionados. Aplicacoes de IA."}, {"Disciplina": "FUNDAMENTOS LOGICOS DE INTELIGENCIA ARTIFICIAL", "Unidade responsavel": "CAMPUS UNB GAMA: FACULDADE DE CIENCIAS E TECNOLOGIAS EM ENGENHARIA", "Ementa": "Introducao a logica classica;; Logica de primeira ordem;; Representacoes proposicionais;; Procedimentos automaticos de prova;; Problema de satisfatibilidade (SAT);; Algoritmos para SAT;; Busca em grafos;; Formas nao clausais de representacao;; Planejamento automatizado;; Aplicacoes em planejamento automatizado."}, {"Disciplina": "NOCOES DE INTELIGENCIA ARTIFICIAL", "Unidade responsavel": "DEPTO ENGENHARIA ELETRICA", "Ementa": "1. Introducao; Historico e Denominacoes; Aprendizado; Redes Neurais; Problemas de interesse.; 2. Aprendizado Supervisionado; Regressao linear; Descida por gradiente; Regressao logistica; Funcoes de custo; Criterios de performance; Entropia cruzada; Vizinhos mais proximos.; 3. Aprendizado Nao-supervisionado; Agrupamento; Reducao de dimensionalidade; Amostragem de Gibbs.; 4. Redes Neurais Artificiais; Perceptron; Perceptron multicamada; Funcoes de Ativacao; Regularizacao.; 5. \"Deep Learning\"; Redes convolucionais; Autocodificadores; Introducao as redes recorrentes.; 6. Outras tecnicas; Algoritmos Geneticos; Logica \"fuzzy\".; 7. Questoes Eticas, Sociais e de Seguranca; Vies; Privacidade; Seguranca; Impactos sociais"}, {"Disciplina": "INTELIGENCIA ARTIFICIAL", "Unidade responsavel": "CAMPUS UNB GAMA: FACULDADE DE CIENCIAS E TECNOLOGIAS EM ENGENHARIA", "Ementa": "DESCRICAO:O estado da arte em IA. Engenharia do conhecimento. Ontologias. Arquiteturas de sistemas baseados em conhecimento. Metodologias para desenvolvimento de sistemas inteligentes. Paradigmas simbolico, conexionista, evolucionario e hibrido. Outros assuntos relevantes dependendo o periodo e ano a ser ministrada esta disciplina. Aplicacoes. Projeto."}]