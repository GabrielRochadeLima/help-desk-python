numeros_chamados = 1

def abrir_chamado(numeros_chamados):
    print("Chamado aberto com sucesso!")
    print("Número do chamado: ", numeros_chamados)
    numeros_chamados += 1

    return numeros_chamados


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



