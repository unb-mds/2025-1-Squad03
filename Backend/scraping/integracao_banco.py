import os
import json
from supabase import create_client, Client
import time
from tenacity import retry, stop_after_attempt, wait_exponential

SUPABASE_URL = "https://lijmhbstgdinsukovyfl.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxpam1oYnN0Z2RpbnN1a292eWZsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NzgzOTM3MywiZXhwIjoyMDYzNDE1MzczfQ._o2wq5p0C6YBIrTGJsNl6xdg4l8Ju7CbwvaaeCWbeAc"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def reconectar_supabase():
    global supabase
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def executar_operacao(operacao, *args, **kwargs):
    try:
        return operacao(*args, **kwargs)
    except Exception as e:
        print(f"Erro na operação: {str(e)}")
        print("Tentando reconectar...")
        reconectar_supabase()
        time.sleep(2)  # Espera 2 segundos antes de tentar novamente
        raise  # Re-lança a exceção para o retry

# Teste de conexão com o Supabase
try:
    resposta = executar_operacao(supabase.table('cursos').select('id, nome').limit(1).execute)
    print('Conexão com Supabase bem-sucedida! Exemplo de curso:', resposta.data)
except Exception as e:
    print('Erro ao conectar com o Supabase. Verifique sua SUPABASE_URL e SUPABASE_KEY.')
    print('Detalhes do erro:', e)

pasta = os.path.join(os.path.dirname(__file__), '..', 'dados', 'estruturas-curriculares')

# Função para recarregar caches do banco
def recarregar_caches():
    cursos_existentes = {}
    result = executar_operacao(supabase.table('cursos').select('id, nome').execute)
    if result.data:
        for c in result.data:
            cursos_existentes[c['nome']] = c['id']

    niveis_existentes = {}
    result = executar_operacao(supabase.table('niveis').select('id, nome, curso_id').execute)
    if result.data:
        for n in result.data:
            niveis_existentes[(n['nome'], n['curso_id'])] = n['id']

    materias_existentes = {}
    result = executar_operacao(supabase.table('materias').select('id, codigo').execute)
    if result.data:
        for m in result.data:
            materias_existentes[m['codigo']] = m['id']

    materias_niveis_existentes = set()
    result = executar_operacao(supabase.table('materias_niveis').select('materia_id, nivel_id').execute)
    if result.data:
        for mn in result.data:
            materias_niveis_existentes.add((mn['materia_id'], mn['nivel_id']))
    return cursos_existentes, niveis_existentes, materias_existentes, materias_niveis_existentes

# Recarregar caches do banco antes de processar
cursos_existentes, niveis_existentes, materias_existentes, materias_niveis_existentes = recarregar_caches()

for arquivo in os.listdir(pasta):
    if arquivo.endswith('.json'):
        with open(os.path.join(pasta, arquivo), 'r', encoding='utf-8') as f:
            dados = json.load(f)
            curso_nome = dados['curso']
            niveis = dados['niveis']

            # Curso
            if curso_nome in cursos_existentes:
                curso_id = cursos_existentes[curso_nome]
                print(f"[DEBUG] Curso já existe: {curso_nome} (id: {curso_id})")
            else:
                curso_id = executar_operacao(supabase.table('cursos').insert({'nome': curso_nome}).execute).data[0]['id']
                cursos_existentes[curso_nome] = curso_id
                print(f"[DEBUG] Inserindo novo curso: {curso_nome} (id: {curso_id})")

            nivel_chaves = set()
            for ordem, nivel in enumerate(niveis, start=1):
                nivel_nome = nivel['nivel']
                chave = (nivel_nome, curso_id)
                if chave in nivel_chaves:
                    print(f"[DEBUG] Nível já processado: {nivel_nome} para curso {curso_nome}")
                    continue  # já processou esse nível para esse curso
                nivel_chaves.add(chave)
                if (nivel_nome, curso_id) in niveis_existentes:
                    nivel_id = niveis_existentes[(nivel_nome, curso_id)]
                    print(f"[DEBUG] Nível já existe: {nivel_nome} (id: {nivel_id}) para curso {curso_nome}")
                else:
                    try:
                        nivel_id = executar_operacao(supabase.table('niveis').insert({'nome': nivel_nome, 'curso_id': curso_id, 'ordem': ordem}).execute).data[0]['id']
                        niveis_existentes[(nivel_nome, curso_id)] = nivel_id
                        print(f"[DEBUG] Inserindo novo nível: {nivel_nome} (id: {nivel_id}) para curso {curso_nome}")
                    except Exception as e:
                        if 'duplicate key value violates unique constraint' in str(e):
                            result = executar_operacao(supabase.table('niveis').select('id').eq('nome', nivel_nome).eq('curso_id', curso_id).execute)
                            if result.data:
                                nivel_id = result.data[0]['id']
                                niveis_existentes[(nivel_nome, curso_id)] = nivel_id
                                print(f"[DEBUG] Nível encontrado após erro de duplicidade: {nivel_nome} (id: {nivel_id})")
                            else:
                                raise
                        else:
                            raise

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
                        print(f"[DEBUG] Matéria já existe: {codigo} - {materia['nome']} (id: {materia_id})")
                    else:
                        try:
                            materia_id = executar_operacao(supabase.table('materias').insert({'codigo': codigo, **materia_dict}).execute).data[0]['id']
                            materias_existentes[codigo] = materia_id
                            print(f"[DEBUG] Inserindo nova matéria: {codigo} - {materia['nome']} (id: {materia_id})")
                        except Exception as e:
                            # Se for erro de duplicidade, busca o id no banco
                            if 'duplicate key value violates unique constraint' in str(e):
                                result = executar_operacao(supabase.table('materias').select('id').eq('codigo', codigo).execute)
                                if result.data:
                                    materia_id = result.data[0]['id']
                                    materias_existentes[codigo] = materia_id
                                    print(f"[DEBUG] Matéria encontrada após erro de duplicidade: {codigo} - {materia['nome']} (id: {materia_id})")
                                else:
                                    raise
                            else:
                                raise

                    # Cria relação materia-nivel
                    if (materia_id, nivel_id) not in materias_niveis_existentes:
                        try:
                            rel_id = executar_operacao(supabase.table('materias_niveis').insert({'materia_id': materia_id, 'nivel_id': nivel_id}).execute).data[0]['id']
                            materias_niveis_existentes.add((materia_id, nivel_id))
                            print(f"[DEBUG] Relacionando materia_id: {materia_id} com nivel_id: {nivel_id} (materias_niveis.id: {rel_id})")
                        except Exception as e:
                            if 'duplicate key value violates unique constraint' in str(e):
                                print(f"[DEBUG] Relação já existe: materia_id: {materia_id} com nivel_id: {nivel_id}")
                            else:
                                raise
                    else:
                        print(f"[DEBUG] Relação já existe: materia_id: {materia_id} com nivel_id: {nivel_id}")
