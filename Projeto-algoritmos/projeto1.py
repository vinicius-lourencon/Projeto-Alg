from cadastrar_aluno import cadastrar_aluno
from cadastrar_professor import cadastrar_professor
from cadastrar_disciplina import cadastrar_disciplina
from cadastrar_turma import cadastrar_turma
from alocar_professor import alocar_professor
from filtrar_professores import filtrar_professores
from matricular_aluno import matricular_aluno
from ver_turmas import ver_turmas


alunos = []
professores = []
disciplinas = []
turmas = []

def menu():
    while True:
        print("--- Sistema de Gerenciamento Acadêmico ---")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Professor")
        print("3. Cadastrar Disciplina")
        print("4. Cadastrar Turma")
        print("5. Alocar Professor a Disciplina")
        print("6. Matricular Aluno em Turma")
        print("7. Filtrar Professores por Disciplina")
        print("8. Ver Turmas")
        print("9. Sair")

        try:
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                cadastrar_aluno(alunos)
            elif opcao == "2":
                cadastrar_professor(professores)
            elif opcao == "3":
                cadastrar_disciplina(disciplinas, professores)
            elif opcao == "4":
                cadastrar_turma(turmas, disciplinas, professores)
            elif opcao == "5":
                alocar_professor(disciplinas, professores)
            elif opcao == "6":
                matricular_aluno(turmas, alunos)
            elif opcao == "7":
                filtrar_professores(disciplinas, professores)
            elif opcao == "8":
                ver_turmas(turmas, disciplinas, professores, alunos)
            elif opcao == "9":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}. Tente novamente.")

menu()
