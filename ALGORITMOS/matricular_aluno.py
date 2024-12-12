from cadastrar_turma import turmas
from cadastrar_aluno import alunos

def matricular_aluno():
    print("=== Matrícula de Aluno em Turma ===")
    matricula = input("Matrícula do Aluno: ")
    codigo_turma = input("Código da Turma: ")

    aluno = next((a for a in alunos if a["matricula"] == matricula), None)
    turma = next((t for t in turmas if t["codigo"] == codigo_turma), None)

    if aluno and turma:
        turma["alunos"].append(matricula)
        print(f"Aluno {aluno['nome']} matriculado na turma {turma['nome']} com sucesso!")
    else:
        print("Aluno ou turma não encontrados.")