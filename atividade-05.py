print("Escolha a temperatura a ser convertida (Números inteiros)")

while True:
    temp = input(": ")
    if not temp.isnumeric() : # Verifica se a variável temp é um número
        print("Somente números")
    else:
        temp = int(temp) # Converte a variável em inteiro
        break

while True:
    print("\nAgora qual o tipo de conversão será feita (0,1)? ")
    print("[0] - Celsius     -> Fahreinheit")
    print("[1] - Fahreinheit -> Celsius")

    conv = input(": ")

    # Verifica se a variável é um inteiro
    if not conv.isnumeric() or not (int(conv) == 0 or int(conv) == 1):
        print("Escolha um valor aceito.")
    else:
        conv = int(conv)
        break

# Verifica qual conversão será feita, e a realiza.
res = (temp * (9/5) + 32) if (conv == 0) else ((temp-32) * 5/9 )

# Verifica a conversão que foi feita, e a imprime.
print(f"A conversão de {temp} "
      f"{"Celsius" if not conv else "Fahrenheit"} para " # Verifica se a conversão é 0 ou 1
      f"{"Celsius" if conv else "Fahrenheit"} é " # Verifica se a conversão é 0 ou 1, para definir qual foi a conversão
      f"{"%.2f" % res} " # Imprime a conversão de forma formatada, para 2 casas decimais
      f"{"Celsius" if conv else "Fahrenheit"}") # Verifica se a conversão é 0 ou 1, para definir qual foi a conversão