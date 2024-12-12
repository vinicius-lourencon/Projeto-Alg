from cadastrar_disciplina import disciplinas

def filtrar_professores():
    print("=== Filtrar Professores por Disciplina ===")
    nome_disciplina = input("Nome da Disciplina: ")

    professores = [d["professor"] for d in disciplinas if d["nome"] == nome_disciplina]
    
    if professores:
        print(f"Professores responsáveis pela disciplina {nome_disciplina}:")
        for professor in professores:
            print(f"- {professor}")
    else:
        print("Nenhum professor encontrado para essa disciplina.")