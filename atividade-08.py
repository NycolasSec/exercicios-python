from random import randint
num_random = randint(0,9)

print("Pensei em um número, tente adivinhá-lo:")
num_user = int(input())

res = "Acertou" if num_user == num_random else "Errou"

print(f"{res} eu pensei no {num_random}")