from random import randint
import time
end = False

print("Vamos jogar dados ?")

while not end:
    n_vez = input("Digite quantas vezes pretende jogar o dado: ")

    while not str(n_vez).isnumeric() or int(n_vez) < 1:
        print("\nPrecisa ser um número e maior do que um !!!\n")
        n_vez = input("Digite quantas vezes pretende jogar o dado: ")

    n_vez = int (n_vez)

    for i in range(n_vez):
        print("Jogando dado...")
        time.sleep(1)
        print(f"Na jogada {i+1} o número foi {randint(1,6)}")

    print("\nQuer jogar de novo?\n[1] - Sim\nQualquer outra tecla para sair.")
    esc_jog = input()

    end = True if not esc_jog == "1" else False