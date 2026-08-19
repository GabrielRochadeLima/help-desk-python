numeros_chamados = 1

def abrir_chamado(numeros_chamados):
    print("Chamado aberto com sucesso!")
    print("Número do chamado: ", numeros_chamados)
    numeros_chamados += 1

    return numeros_chamados

def menu_inicial():
    print("=====Bem vindo ao Help desk=====")

    print("Escolha uma das opções abaixo:")
    print("1 - Abrir chamado")
    print("2 - Consultar chamados")
    print("3 - Sair")

    numero_digitado = int(input("Digite o número da opção desejada: "))
    if numero_digitado == 1:
        numeros_chamados = abrir_chamado(numeros_chamados)
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
        else:
            op == 2
            menu_inicial()  


       
if __name__ == "__main__":
    main()

