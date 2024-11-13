print("Digite uma palavra e irei verificar se ele é um Palídromo.")

string = str(input("\nDigite a palavra: ")).lower()
string_rev = string[::-1]

if string == string_rev:
    print(f"A string {string} é um palídromo.\nnormal: {string}\nInverso: {string_rev}")
else:
    print(f"A string {string} não é um palídromo.")
