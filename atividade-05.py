print("Escolha a temperatura a ser convertida (Números inteiros): ")
temp = int(input())

print("\nAgora qual o tipo de conversão será feita (0,1)? ")
print("[0] - Celsius     -> Fahreinheit")
print("[1] - Fahreinheit -> Celsius")
conv = int(input())

# Verifica qual conversão será feita, e a realiza.
res = (temp * (9/5) + 32) if (conv == 0) else ((temp-32) * 5/9 )

# Verifica a conversão que foi feita, e a imprime.
print(f"A conversão de {temp} {"Celsius" if not conv else "Fahrenheit"} para {"Celsius" if conv else "Fahrenheit"} é {"%.2f" % res} {"Celsius" if conv else "Fahrenheit"}")