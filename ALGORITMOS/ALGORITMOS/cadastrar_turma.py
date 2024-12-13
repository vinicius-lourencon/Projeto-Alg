from dados import turmas, disciplinas, professores

def cadastrar_turma():
    print("=== Cadastro de Turma ===")

    nome = input("Digite o nome da turma: ")
    codigo = input("Digite o código da turma: ")

    if len(disciplinas) == 0:
        print("Nenhuma disciplina cadastrada. Cadastre uma disciplina antes de continuar.")
        return

    print("Disciplinas Disponíveis:")
    for i, disciplina in enumerate(disciplinas):
        print(f"{i + 1} - {disciplina['nome']} (Código: {disciplina['codigo']})")

    while True:
        escolha_disciplina = input("Selecione o número da disciplina: ")
        if escolha_disciplina.isdigit() and 1 <= int(escolha_disciplina) <= len(disciplinas):
            disciplina_selecionada = disciplinas[int(escolha_disciplina) - 1]
            break
        else:
            print("Opção inválida. Tente novamente.")

    if len(professores) == 0:
        print("Nenhum professor cadastrado. Cadastre um professor antes de continuar.")
        return

    print("Professores Disponíveis:")
    for i, professor in enumerate(professores):
        print(f"{i + 1} - {professor['nome']} (Matrícula: {professor['matricula']})")

    while True:
        escolha_professor = input("Selecione o número do professor responsável: ")
        if escolha_professor.isdigit() and 1 <= int(escolha_professor) <= len(professores):
            professor_selecionado = professores[int(escolha_professor) - 1]
            break
        else:
            print("Opção inválida. Tente novamente.")

    turma = {
        "nome": nome,
        "codigo": codigo,
        "disciplina": disciplina_selecionada['codigo'],
        "professor": professor_selecionado['matricula'],
        "alunos": []
    }

    turmas.append(turma)
    print(f"Turma {nome} cadastrada com sucesso!")