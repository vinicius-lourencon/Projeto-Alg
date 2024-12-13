from dados import alunos

def cadastrar_aluno():
    print("=== Cadastro de Aluno ===")

    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    data_nascimento = input("Digite a data de nascimento do aluno (DD/MM/AAAA): ")
    sexo = input("Digite o sexo do aluno (M/F): ")
    endereco = input("Digite o endereço do aluno: ")
    telefone = input("Digite o telefone do aluno: ")
    email = input("Digite o e-mail do aluno: ")

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email
    }

    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")