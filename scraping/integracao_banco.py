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

def get_or_create(table, unique_field, value, extra_fields=None):
    # Busca pelo valor único
    result = supabase.table(table).select("id").eq(unique_field, value).execute()
    if result.data:
        return result.data[0]['id']
    # Cria se não existir
    data = {unique_field: value}
    if extra_fields:
        data.update(extra_fields)
    result = supabase.table(table).insert(data).execute()
    return result.data[0]['id']

def get_or_create_materia_nivel(materia_id, nivel_id):
    result = supabase.table('materias_niveis').select('id').eq('materia_id', materia_id).eq('nivel_id', nivel_id).execute()
    if result.data:
        return result.data[0]['id']
    result = supabase.table('materias_niveis').insert({
        'materia_id': materia_id,
        'nivel_id': nivel_id
    }).execute()
    return result.data[0]['id']

def safe_get_or_create(*args, **kwargs):
    for tentativa in range(3):
        try:
            return get_or_create(*args, **kwargs)
        except Exception as e:
            print(f'[ERRO] Falha ao inserir {args}, tentativa {tentativa+1}/3. Erro: {e}')
            time.sleep(2)  # espera 2 segundos antes de tentar de novo
    raise Exception('Falha após 3 tentativas!')

def safe_get_or_create_materia_nivel(*args, **kwargs):
    for tentativa in range(3):
        try:
            return get_or_create_materia_nivel(*args, **kwargs)
        except Exception as e:
            print(f'[ERRO] Falha ao inserir relação materia-nivel, tentativa {tentativa+1}/3. Erro: {e}')
            time.sleep(2)
    raise Exception('Falha após 3 tentativas!')

for arquivo in os.listdir(pasta):
    if arquivo.endswith('.json'):
        with open(os.path.join(pasta, arquivo), 'r', encoding='utf-8') as f:
            dados = json.load(f)
            curso_nome = dados['curso']
            niveis = dados['niveis']

            curso_id = safe_get_or_create('cursos', 'nome', curso_nome)
            print(f"[DEBUG] Inserindo/obtendo curso: {curso_nome} (id: {curso_id})")

            for ordem, nivel in enumerate(niveis, start=1):
                nivel_nome = nivel['nivel']
                nivel_id = safe_get_or_create('niveis', 'nome', nivel_nome, {'curso_id': curso_id, 'ordem': ordem})
                print(f"[DEBUG] Inserindo/obtendo nível: {nivel_nome} (id: {nivel_id}) para curso_id: {curso_id}, ordem: {ordem}")

                for materia in nivel['materias']:
                    materia_dict = {
                        'nome': materia['nome'],
                        'carga_horaria': materia['carga_horaria'],
                        'natureza': materia['natureza'],
                        'ementa': materia.get('ementa', None),
                    }
                    materia_id = safe_get_or_create('materias', 'codigo', materia['codigo'], materia_dict)
                    print(f"[DEBUG] Inserindo/obtendo matéria: {materia['codigo']} - {materia['nome']} (id: {materia_id})")
                    # Cria relação materia-nivel
                    rel_id = safe_get_or_create_materia_nivel(materia_id, nivel_id)
                    print(f"[DEBUG] Relacionando materia_id: {materia_id} com nivel_id: {nivel_id} (materias_niveis.id: {rel_id})")
                    time.sleep(1)
