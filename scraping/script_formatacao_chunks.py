import json
import os

# Caminho onde estão seus arquivos .json
entrada = "dados_finais"
saida = "chunks_finais"

os.makedirs(saida, exist_ok=True)

# Campos que você quer extrair (edite conforme necessário)
campos = [
    "disciplina",
    "codigo",
    "unidade_responsavel",
    "ementa"

]

def formatar_turma(turma):
    linhas = []
    for campo in campos:
        valor = turma.get(campo, "").strip()
        if valor:
            linhas.append(f"{campo.replace('_', ' ').capitalize()}: {valor}")
    return "\n".join(linhas)

# Para cada arquivo .json na pasta
for nome_arquivo in os.listdir(entrada):
    if nome_arquivo.endswith(".json"):
        with open(os.path.join(entrada, nome_arquivo), "r", encoding="utf-8") as f:
            dados = json.load(f)
        
        chunks = []
        for turma in dados:
            # Gera o texto da turma formatado
            turma_formatada = formatar_turma(turma)
            chunks.append(turma_formatada)

        # Salva um .txt com os chunks separados por 2 quebras de linha
        nome_txt = nome_arquivo.replace(".json", ".txt")
        with open(os.path.join(saida, nome_txt), "w", encoding="utf-8") as out:
            out.write("\n\n\n".join(chunks))
