from random import randint
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '&', '*']
# n_random = randint(0,9)

def passwords(level: int):
    password = ''

    if level == 0:
        for i in range(4):
            password += random.choice(letters)
        for i in range(1):
            password += str(random.choice(numbers))

    elif level == 1:
        for i in range(5):
            n_random = randint(0, 9)
            password += random.choice(letters)
            password += str(random.choice(numbers)) if n_random % 2 == 0 else random.choice(symbols)

    elif level == 2:
        for i in range(8):
            n_random = randint(0, 9)
            password += random.choice(letters) if n_random % 2 == 0 else str(random.choice(letters)).upper()
            n_random = randint(0, 9)
            password += str(random.choice(numbers)) if n_random % 2 == 0 else random.choice(symbols)

    return password

while True:
    print("Qual o nível da senha que você quer gerar ?")
    level = input("[0] - Fraca\n[1] - Média\n[2] - Forte\n: ")

    while not level.isnumeric() or (int(level) < 0 or int(level) > 2):
        print("O nível tem de ser um número!!!\n")
        print("Qual o nível da senha que você quer gerar ?")
        level = input("[0] - Fraca\n[1] - Média\n[2] - Forte\n: ")

    level = int(level)
    print(passwords(level))
