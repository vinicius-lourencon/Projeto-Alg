from dados import turmas, professores, alunos, disciplinas

def ver_turmas():
    print("=== Listagem de Turmas ===")

    if len(turmas) == 0:
        print("Nenhuma turma cadastrada ainda.")
    else:
        for turma in turmas:
            print(f"Turma: {turma['nome']}")
            print(f"Código: {turma['codigo']}")

            for disciplina in disciplinas:
                if disciplina['codigo'] == turma['disciplina']:
                    print(f"Disciplina: {disciplina['nome']}")
                    break

            for professor in professores:
                if professor['matricula'] == turma['professor']:
                    print(f"Professor: {professor['nome']} (Matrícula: {professor['matricula']})")
                    break

            print("Alunos Matriculados:")
            if len(turma['alunos']) == 0:
                print("  Nenhum aluno matriculado.")
            else:
                for matricula in turma['alunos']:
                    for aluno in alunos:
                        if aluno['matricula'] == matricula:
                            print(f"  - {aluno['nome']} (Matrícula: {aluno['matricula']})")
                            break