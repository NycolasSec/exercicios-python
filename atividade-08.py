from random import randint

while True:
    # Gera o número aleatório
    num_random = randint(0, 9)

    print("Pensei em um número entre 0 e 10, tente adivinhá-lo:")
    num_user = int(input())

    # Verifica se houve um erro ou acerto
    res = "Acertou" if num_user == num_random else "Errou"

    print(f"{res} eu pensei no {num_random}")

    esc = input("Tente novamente\n[0] - Sim\nQualquer outra tecla para sair.")

    if not esc == "0":
        exit()