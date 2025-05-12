import PyPDF2


nome_pdf = "historico_232014010 (2)"
with open(nome_pdf+'.pdf', "rb") as file:
    leitor = PyPDF2.PdfReader(file)
    texto_total = ""
    for pagina in leitor.pages:
        texto_total += pagina.extract_text() + "\n" 


matricula = str(nome_pdf.split('_')[1])

with open("historico_completo"+matricula+".txt", "w", encoding="utf-8") as output_file:
    output_file.write(texto_total)  

print("Arquivo 'historico_completo.txt' criado com sucesso!")




import re
import json


with open("historico_completo"+matricula+".txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()


disciplinas = []
padrao_status = re.compile(r"\b(APR|REP|MATR|TRANC|CUMP)\b")
padrao_mencao = re.compile(r"\b(SS|MS|MM|MI|II|SR)\b")
padrao_cump = re.compile(r"--\s+CUMP\b")
padrao_materia_cump = re.compile(r"\d{4}\.\d\s+(.+?)\s+--")
#Dra. GLAUCENY CIRNE DE MEDEIROS (60h)03 REP FGA0133 60 89,0 MI
padrao_horas = re.compile(r"\((.+?)\)")
padrao_horas_cump = re.compile(r"[A-Za-z]+\d+\s+(\d+)\s+\d+,\d")

padrao_codigo = re.compile(r"\b[A-Z]{2,}\d{3,}\b")

# extrai informações
for i, linha in enumerate(linhas):
    creditos = 0
    #print(i)
    linha = linha.strip()
    #print(linha)
    #2024.2 INGLÊS INSTRUMENTAL 1 -- CUMP LET0331 60 100,0 - #
    #2024.2 ATIVIDADE COMPLEMENTAR -- CUMP DEG0202 45 100,0 - *

    #Dra. LUIZA YOKO TANEGUTI (60h)13 APR MAT0031 60 100,0 MM

    # Verifica se a linha tem prefixo de professor
    if linha.startswith("Dr.") or linha.startswith("MSc.") or linha.startswith("Dra."):
        print(linha)
        match_status = padrao_status.search(linha)
        #print(match_status) #<re.Match object; span=(41, 44), match='REP'>
        match_mencao = padrao_mencao.findall(linha)
        #print(match_mencao) #['MI']
        #print('------------------------------------------------')
        match_codigo = padrao_codigo.search(linha)

        
        if match_status:
            status = match_status.group(1)
            mencao = match_mencao[-1] if match_mencao else "-"
            nome_disciplina = linhas[i - 1].strip()  # A disciplina está na linha anterior
            texto_aux = ''
            match_horas = padrao_horas.findall(linha)
            match_horas_formatadas = int(match_horas[0].strip('h'))
            creditos = int(match_horas_formatadas/15)

            codigo = match_codigo.group()
            print("Código da matéria:", codigo)

            for i in range(len(nome_disciplina)):
                #print(texto[i])
                if nome_disciplina[i].isalpha():
                    #nome_disciplina = nome_disciplina.strip(texto_aux)
                    nome_disciplina = (nome_disciplina.split(texto_aux))[1]
                    break

                else:
                    texto_aux += nome_disciplina[i]

            disciplinas.append({"nome_disciplina": nome_disciplina, "status": status, "mencao": mencao, "creditos":creditos, "codigo":codigo, "ch":match_horas_formatadas})

    else:
        creditos_cump = 0
        if padrao_cump.search(linha):
            print(linha)
            match_mencao = padrao_mencao.findall(linha)
            print('ACHOU CUMP!!!!!!!')
            print('--------------------------------------------')
            match_cump = padrao_materia_cump.search(linha)

            match_padrao_horas_cump = padrao_horas_cump.search(linha)

            match_codigo = padrao_codigo.search(linha)

            print(match_padrao_horas_cump)
            if match_cump:
                nome_materia_cump = match_cump.group(1).strip()  # Remove espaços extras
                print(nome_materia_cump)  # Saída: "INGLÊS INSTRUMENTAL 1"
                carga_horaria = int(match_padrao_horas_cump.group(1))
                print("Carga horária:", carga_horaria)
                creditos_cump = int((carga_horaria)/15)
                codigo = match_codigo.group()
                print("Código da matéria:", codigo)
                disciplinas.append({"nome_disciplina": nome_materia_cump, "status": 'CUMP', "mencao": '-', "creditos": creditos_cump, "codigo":codigo, "ch":carga_horaria})
            else:
                print("Nome da matéria não encontrado.")



# Salva os resultados em um arquivo JSON
with open("disciplinas" + "_" + matricula + ".json", "w", encoding="utf-8") as json_file:
    json.dump(disciplinas, json_file, ensure_ascii=False, indent=4)

# Exibe os resultados
for disciplina in disciplinas:
    ...
    #print(f"{disciplina['nome_disciplina']} | Status: {disciplina['status']} | Menção: {disciplina['mencao']}")
