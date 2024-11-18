print("Escolha uma sequência de números, e remover as duplicatas.\nCaso tenha terminado apenas tecle a tecla [Enter]")

nums = []
end = False

while(not end):
    num = input("Qual o número: ") # pegamos o input do usuàrio

    if num == '':
        end = True
    elif num.isnumeric(): # Verificamos se é um número e colocamos no array
        nums.append(int(num))
    else:
        print("Apenas números.")

print(f"Lista normal: {nums}")

nums = list(set(nums)) # Retira as duplicatas

print(f"\nLista sem duplicatas: {nums}")
