print("Os números primos entre 1 e 100 são")

primos = []
prod = 0
end = False
div = 0

for i in range(2,100): # Range de 2 até 101
    prod = i # Armazena o número que será testado, para ser decrementado e testado na divisão
    end = False
    div = 0 # Vai contar os divisores de cada número

    while not end:
        prod = prod - 1 # Decrementamos para ser testado na divisão
        if prod == 1 and div == 0: # Testa se o número não tem nenhum divisor.
            primos.append(i)
            end = True
        elif prod == 1:
            end = True
        elif i % prod == 0: # Testa se um número é divisível pelo seu antecessor
            div = div + 1
            end = True


print(primos)
