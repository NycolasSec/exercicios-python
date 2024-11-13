
print('Escolha um número e eu irei calcular o fatorial dele.\n')

numero = int(input('Digite um número (Inteiro): '))

resultado = 1

# Decrementamos o número e o multiplicamos, até que ele se torne 1
for n in range(1, numero+1):
    resultado *= n

print(f'{numero}! é {resultado}')