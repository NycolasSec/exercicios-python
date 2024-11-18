notas = []

print("Qual o valor da primeira nota ?")
notas.append(int(input())) # Recebe o valor do usuário

print("Qual o valor da segunda nota ?")
notas.append(int(input()))

print("Qual o valor da terceira nota ?")
notas.append(int(input()))

print("Qual o valor da quarta nota ?")
notas.append(int(input()))

# Calcula a média das notas
media = sum(notas)/len(notas) # Soma os valores e retorna a média

print(f"A média das notas é {media}")
