print("Escolha uma sequência de números, e irei ordena-los para você.\nCaso tenha terminado apenas tecle a tecla [Enter]")

nums = []
end = False

while(not end):
    num = input("Qual o número: ") # Armazena o input do usuário

    if num == '':
        end = True
    elif num.isnumeric(): # Verificamos se é um nùmero
        nums.append(int(num)) # onvertemos em inteiro e colocamos no array
    else:
        print("Apenas números.")

nums.sort() # Ordenamos o array
print(f"Os números em ordem crescente: {nums}")

