def cadastrar_disciplina(disciplinas, professores):
    print("--- Cadastro de Disciplina ---")

    nome = input("Digite o nome da disciplina: ")
    codigo = input("Digite o código da disciplina: ")
    carga_horaria = input("Digite a carga horária da disciplina: ")

    if len(professores) == 0:
        print("Nenhum professor cadastrado. Cadastre um professor antes de continuar.")
        return

    print("Professores Disponíveis:")
    for i, professor in enumerate(professores):
        print(f"{i + 1} - {professor['nome']} (Matrícula: {professor['matricula']})")

    while True:
        escolha = input("Selecione o número do professor responsável: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(professores):
            professor_selecionado = professores[int(escolha) - 1]
            break
        else:
            print("Opção inválida. Tente novamente.")

    disciplina = {
        "nome": nome,
        "codigo": codigo,
        "carga_horaria": carga_horaria,
        "professor": professor_selecionado['matricula']
    }

    disciplinas.append(disciplina)
    print(f"Disciplina {nome} cadastrada com sucesso!")