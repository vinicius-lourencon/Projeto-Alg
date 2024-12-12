professores = []

def cadastrar_professor():
    print("=== Cadastro de Professor ===")
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    sexo = input("Sexo (M/F): ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    professor = {
        "nome": nome,
        "matricula": matricula,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email
    }
    professores.append(professor)
    print("Professor cadastrado com sucesso!")