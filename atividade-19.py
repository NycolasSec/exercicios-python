print("---------- Sistema de cadastro ----------")

end = False
clientes = {}

def show_clientes():
    for i in clientes.keys():
        print(f"\n- Cliente: {i}" # Imprime o dicionário clientes, de forma formatada
              f"\nSexo: {clientes[i]['sexo']}"
              f"\nIdade: {clientes[i]['idade']}")

def ad_cliente():
    # Nome do cliente
    nome = input(f"Qual o nome do cliente? ")
    while nome in clientes.keys() or nome == '': # Verifica se o cliente já existe
        nome = input("Esse cliente já existe ou nulo. Crie com outro nome\n: ")

    # Sexo do cliente
    print("Qual o sexo do cliente?"
          "\n[M] - Masculino"
          "\n[F] - Feminino")
    sexo = input(": ").lower()

    while not sexo == "f" and not sexo == "m":
        print("Escolha entre:"
              "\n[M] - Masculino"
              "\n[F] - Feminino")
        sexo = input(": ").lower() # captura o nome do cliente e transforma em minúsculas

    # Idade do cliente
    idade = input(f"Qual a idade do cliente.\n: ")

    while not idade.isnumeric():
        idade = input("Idade precisa ser um número\n: ")
    int(idade)
    clientes[nome] = {'sexo':sexo, 'idade':idade} # Adiciona mais um elemento no dicionário

def del_cliente():
    nome = input(f"Qual o nome do cliente a ser deletado?\n: ")
    while not nome in clientes.keys() or nome == '': # verifica se o nome do cliente é válido
        nome = input("Cliente não existe ou nulo. Escolha outro nome\n: ")

    clientes.pop(nome)


while not end: # Define o término do programa
    print("\n\nQual ação pretende tomar agora?"
          "\n[0] - Ver clientes atuais."
          "\n[1] - Adicionar cliente."
          "\n[2] - Remover um cliente.")
    act = input(": ")

    while not act.isnumeric() or not (0 <= int(act) <= 2):
        act = input("Digite alguma opção válida\n: ")

    # Verifica a ação a ser tomada
    if act == "0":
        show_clientes()
    elif act == "1":
        ad_cliente()
    elif act == "2":
        del_cliente()