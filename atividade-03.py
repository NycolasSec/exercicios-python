print("Escolha um número: ")
n = int(input()) # Recebe um número do usuário

res = "ímpar" if (n%2) else "par" # Testa se o número é divisível por 2, e retorna par pu ímpar

print(f"O número escolhido é {res}") # Escreve o resultado na tela