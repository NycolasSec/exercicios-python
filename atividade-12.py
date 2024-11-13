print("Escolha uma sequência de números, e remover as duplicatas.\nCaso tenha terminado apenas tecle a tecla [Enter]")

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

print(f"Lista normal: {nums}")

nums = list(set(nums))

print(f"\nLista sem duplicatas: {nums}")
