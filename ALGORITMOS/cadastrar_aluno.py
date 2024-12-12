alunos = []

def cadastrar_aluno():
    print("=== Cadastro de Aluno ===")
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    sexo = input("Sexo (M/F): ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

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
    print("Aluno cadastrado com sucesso!")