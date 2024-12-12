from cadastrar_professor import professores
from cadastrar_disciplina import disciplinas

def alocar_professor():
    print("=== Alocar Professor em Disciplina ===")
    nome_professor = input("Nome do Professor: ")
    codigo_disciplina = input("Código da Disciplina: ")

    professor = next((p for p in professores if p["nome"] == nome_professor), None)
    disciplina = next((d for d in disciplinas if d["codigo"] == codigo_disciplina), None)

    if professor and disciplina:
        disciplina["professor"] = nome_professor
        print(f"Professor {nome_professor} alocado à disciplina {disciplina['nome']} com sucesso!")
    else:
        print("Professor ou disciplina não encontrados.")