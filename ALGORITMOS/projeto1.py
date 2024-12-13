'''- Crie um sistema escolar que permita cadastrar alunos, professores, disciplinas e turmas.
    Usuários:
        - Alunos: Nome, matrícula, data de nascimento, sexo, endereço, telefone e e-mail.
            ******************************************************************
            - O sistema deve permitir a matricula de alunos em turmas.
        
        - Professores: nome, matrícula, data de nascimento, sexo, endereço, telefone e e-mail
            ******************************************************************       
            - O sistema deve permitir a alocação de professores em disciplinas.
                        
    - Disciplinas: nome, código (UUID), carga horária, professor.
    - Turmas: nome, código (A1234), disciplina, professor, alunos (lista-matricula)

    - O sistema deve permitir a filtragem de professores por disciplina.'''
    
import cadastrar_aluno
import cadastrar_professor
import cadastrar_disciplina
import cadastrar_turma
import alocar_professor
import filtrar_professores
import matricular_aluno
import ver_turmas


alunos = []  
professores = []  
disciplinas = []  
turmas = []


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

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            cadastrar_professor()
        elif opcao == "3":
            cadastrar_disciplina()
        elif opcao == "4":
            cadastrar_turma()
        elif opcao == "5":
            alocar_professor()
        elif opcao == "6":
            matricular_aluno()
        elif opcao == "7":
            filtrar_professores()
        elif opcao == "8":
            ver_turmas()
        elif opcao == "9":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
