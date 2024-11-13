num = int(input("Escolha um número:"))
print("A tabuada desse número é a seguinte\n")

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")