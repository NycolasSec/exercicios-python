num = int(input("Escolha um número:")) # Recebe o input do usuário e converte em um inteiro
print("A tabuada desse número é a seguinte\n")

for i in range(1,11): # Faz uma iteração de 1 a 10
    print(f"{num} x {i} = {num*i}") # Retorna o produto do número do usuário com o número da iteração