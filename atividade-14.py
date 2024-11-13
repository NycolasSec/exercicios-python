print("Digite uma palavra e irei verificar se ele é um Palídromo.")

string = str(input("\nDigite a palavra: ")).lower()
string_rev = string[::-1] # Armazena a inversão da string

if string == string_rev: # verifica se a string é igual ao seu inverso
    print(f"A string {string} é um palídromo.\nnormal: {string}\nInverso: {string_rev}")
else:
    print(f"A string {string} não é um palídromo.")
