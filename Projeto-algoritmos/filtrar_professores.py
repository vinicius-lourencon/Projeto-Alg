def filtrar_professores(disciplinas, professores):
    print("=== Filtrar Professores por Disciplina ===")

    if len(disciplinas) == 0:
        print("Nenhuma disciplina cadastrada.")
        return

    print("Disciplinas disponíveis:")
    for i, disciplina in enumerate(disciplinas):
        print(f"{i + 1}. {disciplina['nome']}")

    try:
        opcao = int(input("Escolha uma disciplina pelo número: ")) - 1
        if opcao < 0 or opcao >= len(disciplinas):
            print("Opção inválida.")
            return

        disciplina_selecionada = disciplinas[opcao]
        print(f"Professores responsáveis pela disciplina {disciplina_selecionada['nome']}:")

        encontrou = False
        for professor in professores:
            if professor['matricula'] == disciplina_selecionada['professor']:
                print(f"- {professor['nome']} (Matrícula: {professor['matricula']})")
                encontrou = True

        if not encontrou:
            print("Nenhum professor alocado para esta disciplina.")

    except ValueError:
        print("Entrada inválida. Escolha um número válido.")
