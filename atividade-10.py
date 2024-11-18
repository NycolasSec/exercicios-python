print("Escolha uma sequência de números, e irei soma-los para você,\ncaso tenha terminado apenas tecle a tecla [Enter]")

nums = []
end = False

while(not end):
    num = input("Qual o número: ") # Armazena o input do usuário e converte para inteiro

    if num == '':
        end = True
    elif num.isnumeric(): # Verificamos se é um  número, e colocamos no array nums.
        nums.append(int(num))
    else:
        print("Apenas números.")

print(f"A soma de todos os números é {sum(nums)}") # Retorna a soma de todos os números do array