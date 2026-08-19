numeros_chamados = 1

def abrir_chamado():
    try:
        with open("chamados.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        numeros_chamados = len(linhas) + 1
    except FileNotFoundError:
        numeros_chamados = 1    
    print("Chamado aberto com sucesso!")
    print("Número do chamado: ", numeros_chamados)

    titulo = input("Digite o título do chamado: ")

    with open("chamados.txt", "a") as arquivo:
        arquivo.write(f"Chamado {numeros_chamados}: {titulo}\n")

def menu_inicial():
    print("=====Bem vindo ao Help desk=====")

    print("Escolha uma das opções abaixo:")
    print("1 - Abrir chamado")
    print("2 - Consultar chamados")
    print("3 - Sair")

    numero_digitado = int(input("Digite o número da opção desejada: "))
    if numero_digitado == 1:
        abrir_chamado()
    elif numero_digitado == 2:
        print("Consultando chamados...")
    elif numero_digitado == 3:
        print("Saindo...")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    print(f"Usuário {nome} cadastrado com sucesso!")

def main():
    while True:
        print("Olá usuário! Bem vindo ao help desk!")
        print("É a sua primeira vez aqui?")
        op= int(input("Digite 1 para sim e 2 para não: "))
        if op == 1:
            print("Seja bem vindo!")
            cadastrar_usuario()
        elif op == 2:
            print("Seja bem vindo de volta!")
            menu_inicial()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")    


       
if __name__ == "__main__":
    main()

