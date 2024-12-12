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
import matricular_aluno
import alocar_professor
import filtrar_professores


def main():
    while True:
        print("=== Sistema Escolar ===")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Professor")
        print("3. Cadastrar Disciplina")
        print("4. Cadastrar Turma")
        print("5. Matricular Aluno em Turma")
        print("6. Alocar Professor em Disciplina")
        print("7. Filtrar Professores por Disciplina")
        print("8. Ver Turmas")
        print("0. Sair")

        opcao = input("Escolha uma opcão: ")

        if opcao == "1":
            cadastrar_aluno.cadastrar_aluno()
        elif opcao == "2":
            cadastrar_professor.cadastrar_professor()
        elif opcao == "3":
            cadastrar_disciplina.cadastrar_disciplina()
        elif opcao == "4":
            cadastrar_turma.cadastrar_turma()
        elif opcao == "5":
            matricular_aluno.matricular_aluno()
        elif opcao == "6":
            alocar_professor.alocar_professor()
        elif opcao == "7":
            filtrar_professores.filtrar_professores()
        elif opcao == "0":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
