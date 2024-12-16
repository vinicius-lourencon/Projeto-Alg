def cadastrar_professor(professores):
    print("--- Cadastro de Professor ---")

    nome = input("Digite o nome do professor: ")
    matricula = input("Digite a matrícula do professor: ")
    data_nascimento = input("Digite a data de nascimento do professor (DD/MM/AAAA): ")
    sexo = input("Digite o sexo do professor (M/F): ")
    endereco = input("Digite o endereço do professor: ")
    telefone = input("Digite o telefone do professor: ")
    email = input("Digite o e-mail do professor: ")

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
    print(f"Professor {nome} cadastrado com sucesso!")