notas = []

print("Qual o valor da primeira nota ?")
notas.append(int(input()))

print("Qual o valor da segunda nota ?")
notas.append(int(input()))

print("Qual o valor da terceira nota ?")
notas.append(int(input()))

print("Qual o valor da quarta nota ?")
notas.append(int(input()))

media = sum(notas)/len(notas)

print(f"A média das notas é {media}")
