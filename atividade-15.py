print("Os números primos entre 1 e 100 são")

primos = []
prod = 0
end = False
div = 0

for i in range(2,100):
    prod = i
    end = False
    div = 0

    while (not end):
        prod = prod - 1
        if (prod == 1 and div == 0):
            primos.append(i)
            end = True
        elif (prod == 1):
            end = True
        elif i % prod == 0:
            div = div + 1
            end = True


print(primos)
