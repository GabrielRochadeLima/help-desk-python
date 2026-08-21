def abrir_chamado():
    try:
        with open("chamados.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        numero_chamado = len(linhas) + 1

    except FileNotFoundError:
        numero_chamado = 1

    titulo = input("Digite o título do chamado: ")
    descricao = input("Digite a descrição do chamado: ")
    prioridade = input("Digite a prioridade do chamado (Baixa, Média, Alta): ")
    setor = input("Digite o setor responsável pelo chamado: ")
    impacto = input("Digite o impacto do chamado (Baixo, Médio, Alto): ")
    data_limite = input("Digite a data limite para resolução do chamado (dd/mm/aaaa): ")


    with open("chamados.txt", "a") as arquivo:
        arquivo.write(
            f"Chamado {numero_chamado}: {titulo} - {descricao} - {prioridade} - {setor} - {impacto} - {data_limite}\n"
        )

    print("Chamado aberto com sucesso!")
    print("Número do chamado:", numero_chamado)


def menu_inicial():
    print("\n===== Bem vindo ao Help Desk =====")
    print("1 - Login")
    print("2 - Cadastrar usuário")
    print("3 - Sair")

    numero_digitado = int(
        input("Digite o número da opção desejada: ")
    )

    if numero_digitado == 1:
        login()

    elif numero_digitado == 2:
        cadastrar_usuario()

    elif numero_digitado == 3:
        print("Saindo...")
        return False

    else:
        print("Opção inválida.")

    return True

def menu_chamados():
    while True:
        print("\n===== Menu Help Desk =====")
        print("1 - Abrir chamado")
        print("2 - Consultar chamados")
        print("3 - Sair")

        numero_digitado = int(
            input("Digite o número da opção desejada: ")
        )

        if numero_digitado == 1:
            abrir_chamado()

        elif numero_digitado == 2:
            print("Consultando chamados...")

        elif numero_digitado == 3:
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


def login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    try:
        with open("usuarios.txt", "r") as arquivo:
            usuarios = arquivo.readlines()

        for usuario in usuarios:
            nome_usuario, email_usuario, senha_usuario = usuario.strip().split(",")

            if email == email_usuario and senha == senha_usuario:
               print(f"\nLogin realizado com sucesso para o usuário {nome_usuario}!")
               menu_chamados()
               return
        print("\nEmail ou senha incorretos. Tente novamente.")
    except FileNotFoundError:
        print("\nNenhum usuário cadastrado. Por favor, cadastre-se primeiro.")     
    print(
        f"\nLogin realizado com sucesso para o usuário "
        f"{nome_usuario}!"
    )

    menu_chamados()


def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    print(
        f"\nUsuário {nome} cadastrado com sucesso!")
    
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{email},{senha}\n")


def main():
    while True:
        continuar = menu_inicial()

        if not continuar:
            break


if __name__ == "__main__":
    main()