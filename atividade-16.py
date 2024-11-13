from random import randint

print("---------- Jogo da forca ----------")

words = ["livro","caneta","garfo","panela","mesa","cama","microfone","celular","martelo","bolsa","criança","menina","garoto","pai","mãe","homem","mulher","professor","médica","estudante","ator","empresário","cachorro","gato","cavalo","tigre","papagaio","mico","capivara","palmeira","roseira","samambaia","capim","coqueiro","girassol","goiaba","banana","pitanga","laranja","limão","mamão","montanha","ilha","lago","rio","mangue","serra","bairro","cidade","país","manhã","noite","dia","sol","chuva","vento","mês","século","fada","fantasma","bruxa","sereia","vampiro"]
n_random = randint(0,len(words)-1)
word = list(words[n_random])
c_letter = []
w_letter = []
s_word=list('-' * len(word))
life = 10
end = False

while not end:
    print("\n\n----- ----- -----")

    print(f"Letras restantes: {len(word)}\nTentativas restantes: {life}")
    print(f"Acertos: {c_letter}\nErros:   {w_letter}")

    print(f"\n\nPalavra sercreta: ", end="")
    for n in s_word:print(f"{n}",end="")

    letter = str(input("\nDigite uma letra: "))

    if letter in word:
        if not letter in c_letter:
            c_letter.append(letter)
        for i in range(0, len(word)):
            if letter == word[i]:
                s_word[i] = word[i]
    else:
        if not letter in w_letter:
            w_letter.append(letter)
            life = life - 1


    if word == s_word:
        print("---------- Parabéns, você ganhou. ----------")
        end = True
    elif life == 0:
        print("---------- Que pena, você perdeu. ----------")
        print("A palavra era: ", end="")
        for n in word: print(f"{n}", end="")
        end = True