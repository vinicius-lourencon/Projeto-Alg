turmas = []

def cadastrar_turma():
    print("=== Cadastro de Turma ===")
    nome = input("Nome da Turma: ")
    codigo = input("Código da Turma (ex: A1234): ")
    disciplina = input("Disciplina (nome): ")
    professor = input("Professor (nome): ")

    turma = {
        "nome": nome,
        "codigo": codigo,
        "disciplina": disciplina,
        "professor": professor,
        "alunos": []  # Lista de matrículas de alunos
    }
    turmas.append(turma)
    print("Turma cadastrada com sucesso!")