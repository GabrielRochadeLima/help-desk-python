def area_administrativa():
    while True:
        print("\n===== Área Administrativa =====")
        print("1 - Consultar todos os chamados")
        print("2 - Consultar usuários")
        print("3 - Sair")

        numero_digitado = input("Digite o número da opção desejada: ")

        if numero_digitado == "1":
            consultar_todos_chamados()

        elif numero_digitado == "2":
            consultar_usuarios()

        elif numero_digitado == "3":
            print("Saindo da área administrativa...")
            break

        else:
            print("Opção inválida.")


def consultar_todos_chamados():
    try:
        with open("chamados.txt", "r") as arquivo:
            chamados = arquivo.readlines()
    except FileNotFoundError:
        chamados = []

    if not chamados:
        print("Nenhum chamado encontrado.")
        return

    print("\n===== Todos os Chamados =====")
    for chamado in chamados:
        print(chamado.strip())


def consultar_usuarios():
    try:
        with open("usuarios.txt", "r") as arquivo:
            usuarios = arquivo.readlines()
    except FileNotFoundError:
        usuarios = []

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("\n===== Usuários Cadastrados =====")
    for usuario in usuarios:
        dados_usuario = usuario.strip().split(",")

        if len(dados_usuario) not in (3, 4):
            print("Registro de usuário inválido ignorado.")
            continue

        nome_usuario, email_usuario, _ = dados_usuario[:3]
        tipo_usuario = dados_usuario[3].strip() if len(dados_usuario) == 4 else "usuario"
        print(f"Nome: {nome_usuario.strip()} | E-mail: {email_usuario.strip()} | Tipo: {tipo_usuario}")

def abrir_chamado(usuario_logado):
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
            f"Chamado {numero_chamado}, {usuario_logado}, {titulo}, {descricao}, {prioridade}, {setor}, {impacto}, {data_limite}\n"
        )

    print("Chamado aberto com sucesso!")
    print("Número do chamado:", numero_chamado)

def consultar_chamados(usuario_logado):
    try:
        with open("chamados.txt", "r") as arquivo:
            chamados = arquivo.readlines()
        encontrou_chamados = False
        for chamado in chamados:
            dados_chamado = chamado.strip().split(", ")
            usuario = dados_chamado[1].strip()
            if usuario == usuario_logado:
                encontrou_chamados = True
                print(chamado.strip())
        if not encontrou_chamados:
            print("Nenhum chamado encontrado.")

    except FileNotFoundError:
        print("Nenhum chamado encontrado.")

def menu_inicial():
    print("\n===== Bem vindo ao Help Desk =====")
    print("1 - Login")
    print("2 - Cadastrar usuário")
    print("3 - Area Administrativa")
    print("4 - Sair")

    numero_digitado = int(
        input("Digite o número da opção desejada: ")
    )

    if numero_digitado == 1:
        usuario_logado = login()
        if usuario_logado:
            menu_chamados(usuario_logado)

    elif numero_digitado == 2:
        cadastrar_usuario()

    elif numero_digitado == 3:
        autenticar_administrador()

    elif numero_digitado == 4:
        print("Saindo...")
        return False

    else:
        print("Opção inválida.")

    return True

def menu_chamados(usuario_logado):
    while True:
        print(f"\n===== Menu Help Desk - Usuário: {usuario_logado} =====")
        print("1 - Abrir chamado")
        print("2 - Consultar chamados")
        print("3 - Sair")

        numero_digitado = int(
            input("Digite o número da opção desejada: ")
        )

        if numero_digitado == 1:
            abrir_chamado(usuario_logado)

        elif numero_digitado == 2:
            print("Consultando chamados...")
            consultar_chamados(usuario_logado)

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
            dados_usuario = usuario.strip().split(",")
            if len(dados_usuario) not in (3, 4):
                continue

            nome_usuario, email_usuario, senha_usuario = dados_usuario[:3]

            if email == email_usuario and senha == senha_usuario:
               print(f"\nLogin realizado com sucesso para o usuário {nome_usuario}!")
               return nome_usuario
            
        print("\nEmail ou senha incorretos. Tente novamente.")
    except FileNotFoundError:
        print("\nNenhum usuário cadastrado. Por favor, cadastre-se primeiro.")     
    return None

def autenticar_administrador():
    print("\n===== Autenticacao de Administrador =====")
    email = input("Digite o email do administrador: ")
    senha = input("Digite a senha do administrador: ")

    try:
        with open("usuarios.txt", "r") as arquivo:
            usuarios = arquivo.readlines()

        for usuario in usuarios:
            dados_usuario = usuario.strip().split(",")

            if len(dados_usuario) != 4:
                continue

            _, email_usuario, senha_usuario, tipo_usuario = dados_usuario

            if email == email_usuario and senha == senha_usuario:
                if tipo_usuario.strip() == "admin":
                    print("\nAutenticacao de administrador realizada com sucesso!")
                    area_administrativa()
                else:
                    print("\nAcesso negado. Voce nao possui permissao de administrador.")
                return

        print("\nEmail ou senha incorretos. Tente novamente.")
    except FileNotFoundError:
        print("\nNenhum usuario cadastrado. Por favor, cadastre-se primeiro.")


def exists_in_file(email):
    try:
        with open("usuarios.txt", "r") as arquivo:
            usuarios = arquivo.readlines()

        for usuario in usuarios:
            dados_usuario = usuario.strip().split(",")
            if len(dados_usuario) not in (3, 4):
                continue

            email_usuario = dados_usuario[1]
            if email == email_usuario:
                return True
    except FileNotFoundError:
        return False

    return False

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    tipo_usuario = input("Digite o tipo de usuario (usuario ou admin): ").lower()

    if not nome or not email or not senha or not tipo_usuario:
        print("\nTodos os campos são obrigatórios. Tente novamente.")
        return
    if tipo_usuario not in ("usuario", "admin"):
        print("\nTipo de usuario invalido. Use usuario ou admin.")
        return
    if exists_in_file(email):
        print("\nEmail já cadastrado. Tente novamente.")
        return

    
    
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{email},{senha},{tipo_usuario}\n")

    print(f"\nUsuário {nome} cadastrado com sucesso!")


def main():
    while True:
        continuar = menu_inicial()

        if not continuar:
            break


if __name__ == "__main__":
    main()
