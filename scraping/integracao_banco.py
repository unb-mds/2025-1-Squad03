import os
import json
from supabase import create_client, Client
import time

SUPABASE_URL = "https://lijmhbstgdinsukovyfl.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxpam1oYnN0Z2RpbnN1a292eWZsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NzgzOTM3MywiZXhwIjoyMDYzNDE1MzczfQ._o2wq5p0C6YBIrTGJsNl6xdg4l8Ju7CbwvaaeCWbeAc"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Teste de conexão com o Supabase
try:
    resposta = supabase.table('cursos').select('id, nome').limit(1).execute()
    print('Conexão com Supabase bem-sucedida! Exemplo de curso:', resposta.data)
except Exception as e:
    print('Erro ao conectar com o Supabase. Verifique sua SUPABASE_URL e SUPABASE_KEY.')
    print('Detalhes do erro:', e)

pasta = os.path.join(os.path.dirname(__file__), '..', 'dados', 'estruturas-curriculares')

# Carregar cursos existentes
cursos_existentes = {}
result = supabase.table('cursos').select('id, nome').execute()
if result.data:
    for c in result.data:
        cursos_existentes[c['nome']] = c['id']

# Carregar níveis existentes
niveis_existentes = {}
result = supabase.table('niveis').select('id, nome, curso_id').execute()
if result.data:
    for n in result.data:
        niveis_existentes[(n['nome'], n['curso_id'])] = n['id']

# Carregar matérias existentes
materias_existentes = {}
result = supabase.table('materias').select('id, codigo').execute()
if result.data:
    for m in result.data:
        materias_existentes[m['codigo']] = m['id']

# Carregar relações materias_niveis existentes
materias_niveis_existentes = set()
result = supabase.table('materias_niveis').select('materia_id, nivel_id').execute()
if result.data:
    for mn in result.data:
        materias_niveis_existentes.add((mn['materia_id'], mn['nivel_id']))

for arquivo in os.listdir(pasta):
    if arquivo.endswith('.json'):
        with open(os.path.join(pasta, arquivo), 'r', encoding='utf-8') as f:
            dados = json.load(f)
            curso_nome = dados['curso']
            niveis = dados['niveis']

            # Curso
            if curso_nome in cursos_existentes:
                curso_id = cursos_existentes[curso_nome]
            else:
                curso_id = supabase.table('cursos').insert({'nome': curso_nome}).execute().data[0]['id']
                cursos_existentes[curso_nome] = curso_id
            print(f"[DEBUG] Inserindo/obtendo curso: {curso_nome} (id: {curso_id})")

            for ordem, nivel in enumerate(niveis, start=1):
                nivel_nome = nivel['nivel']
                if (nivel_nome, curso_id) in niveis_existentes:
                    nivel_id = niveis_existentes[(nivel_nome, curso_id)]
                else:
                    nivel_id = supabase.table('niveis').insert({'nome': nivel_nome, 'curso_id': curso_id, 'ordem': ordem}).execute().data[0]['id']
                    niveis_existentes[(nivel_nome, curso_id)] = nivel_id
                print(f"[DEBUG] Inserindo/obtendo nível: {nivel_nome} (id: {nivel_id}) para curso_id: {curso_id}, ordem: {ordem}")

                for materia in nivel['materias']:
                    materia_dict = {
                        'nome': materia['nome'],
                        'carga_horaria': materia['carga_horaria'],
                        'natureza': materia['natureza'],
                        'ementa': materia.get('ementa', None),
                    }
                    codigo = materia['codigo']
                    if codigo in materias_existentes:
                        materia_id = materias_existentes[codigo]
                    else:
                        materia_id = supabase.table('materias').insert({'codigo': codigo, **materia_dict}).execute().data[0]['id']
                        materias_existentes[codigo] = materia_id
                    print(f"[DEBUG] Inserindo/obtendo matéria: {codigo} - {materia['nome']} (id: {materia_id})")
                    # Cria relação materia-nivel
                    if (materia_id, nivel_id) not in materias_niveis_existentes:
                        rel_id = supabase.table('materias_niveis').insert({'materia_id': materia_id, 'nivel_id': nivel_id}).execute().data[0]['id']
                        materias_niveis_existentes.add((materia_id, nivel_id))
                        print(f"[DEBUG] Relacionando materia_id: {materia_id} com nivel_id: {nivel_id} (materias_niveis.id: {rel_id})")
                 
