from projeto1 import turmas, alunos

def matricular_aluno():
    print("--- Matricular Aluno em Turma ---")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado. Cadastre um aluno antes de continuar.")
        return

    if len(turmas) == 0:
        print("Nenhuma turma cadastrada. Cadastre uma turma antes de continuar.")
        return

    print("Alunos Disponíveis:")
    for i, aluno in enumerate(alunos):
        print(f"{i + 1} - {aluno['nome']} (Matrícula: {aluno['matricula']})")

    while True:
        escolha_aluno = input("Selecione o número do aluno: ")
        if escolha_aluno.isdigit() and 1 <= int(escolha_aluno) <= len(alunos):
            aluno_selecionado = alunos[int(escolha_aluno) - 1]
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("Turmas Disponíveis:")
    for i, turma in enumerate(turmas):
        print(f"{i + 1} - {turma['nome']} (Código: {turma['codigo']})")

    while True:
        escolha_turma = input("Selecione o número da turma: ")
        if escolha_turma.isdigit() and 1 <= int(escolha_turma) <= len(turmas):
            turma_selecionada = turmas[int(escolha_turma) - 1]
            break
        else:
            print("Opção inválida. Tente novamente.")

    if aluno_selecionado['matricula'] in turma_selecionada['alunos']:
        print("O aluno já está matriculado nesta turma.")
    else:
        turma_selecionada['alunos'].append(aluno_selecionado['matricula'])
        print(f"Aluno {aluno_selecionado['nome']} matriculado na turma {turma_selecionada['nome']} com sucesso!")