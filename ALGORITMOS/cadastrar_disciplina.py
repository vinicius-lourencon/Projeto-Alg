import uuid

disciplinas = []

def cadastrar_disciplina():
    print("=== Cadastro de Disciplina ===")
    nome = input("Nome da Disciplina: ")
    carga_horaria = input("Carga Horária (em horas): ")
    professor = input("Professor responsável (nome): ")

    disciplina = {
        "nome": nome,
                "codigo": str(uuid.uuid4()),  # Gera um código único para a disciplina
        "carga_horaria": carga_horaria,
        "professor": professor
    }
    disciplinas.append(disciplina)
    print("Disciplina cadastrada com sucesso!")