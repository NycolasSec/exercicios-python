with open('lista_numeros.txt', 'r') as arquivo:
    conteudo = arquivo.read()

tot = 0

conteudo = conteudo.split(",")

for n in conteudo:
    num = n.lstrip()
    if not num.isnumeric():
        print("Somente números.")
        exit()
    tot += int(num)

print(f"\nSoma total:      {tot}"
      f"\nQtd. de numeros: {len(conteudo)}"
      f"\nMédia:           {"%.3f" % (tot/len(conteudo))}")
