with open('lista_numeros.txt', 'r') as arquivo: # Abrimos, lemos o arquivos e fechamos de forma automática
    conteudo = arquivo.read()

tot = 0

conteudo = conteudo.split(",")

for n in conteudo:
    num = n.strip()
    if not num.isnumeric(): # Verifica se só existe números
        print("Somente números.")
        exit()
    tot += int(num) # Soma o número que foi testado.

print(f"\nSoma total:      {tot}"
      f"\nQtd. de numeros: {len(conteudo)}" # Pega o tamanho do array
      f"\nMédia:           {"%.2f" % (tot/len(conteudo))}") # Retorna a média dos números
