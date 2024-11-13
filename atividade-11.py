print("Escolha uma sequência de números, e irei ordena-los para você.\nCaso tenha terminado apenas tecle a tecla [Enter]")

nums = []
end = False

while(not end):
    num = input("Qual o número: ")

    if num == '':
        end = True
    elif num.isnumeric():
        nums.append(int(num))
    else:
        print("Apenas números.")

nums.sort()
print(f"Os números em ordem crescente: {nums}")

