from random import randint

print("---------- Jogo da forca ----------")

words = ["livro","caneta","garfo","panela","mesa","cama","microfone","celular","martelo","bolsa","criança","menina",
         "garoto","pai","mãe","homem","mulher","professor","médica","estudante","ator","empresário","cachorro","gato",
         "cavalo","tigre","papagaio","mico","capivara","palmeira","roseira","samambaia","capim","coqueiro","girassol",
         "goiaba","banana","pitanga","laranja","limão","mamão","montanha","ilha","lago","rio","mangue","serra","bairro",
         "cidade","país","manhã","noite","dia","sol","chuva","vento","mês","século","fada","fantasma","bruxa","sereia",
         "vampiro"]

n_random = randint(0,len(words)-1) # Seleciona a palavra a ser jogada
word = list(words[n_random])
c_letter = []
w_letter = []
s_word=list('-' * len(word))
life = 10
end = False

while not end:
    print("\n\n----- ----- -----")

    print(f"Letras restantes: {len(word) - len(c_letter)}" # calcula as letras restantes
          f"\nTentativas restantes: {life}")

    print(f"Acertos: {c_letter}\n"
          f"Erros:   {w_letter}")

    print(f"\nPalavra sercreta: ", end="")
    for n in s_word:print(f"{n}",end="")

    letter = str(input("\nDigite uma letra: "))

    if letter in word: # Verifica se a letra digitada, está na palavra escolhida
        if not letter in c_letter:
            c_letter.append(letter)
        for i in range(0, len(word)):
            if letter == word[i]:
                s_word[i] = word[i]
    else:
        if not letter in w_letter: # Verifica se a letra ja esta foi errada para não tirar vidas
            w_letter.append(letter) # adiciona a letra a variavel de letras erradas
            life = life - 1


    if word == s_word: # Se apalavra que descobrimos for igual a selecionada
        print("---------- Parabéns, você ganhou. ----------")
        print("A palavra era: ", end="")
        for n in word: print(f"{n}", end="")
        end = True
    elif life == 0: # Se a nossa vida está zerada
        print("---------- Que pena, você perdeu. ----------")
        print("A palavra era: ", end="")
        for n in word: print(f"{n}", end="") # itera a a palavra escolhida para mostrar na tela
        end = True