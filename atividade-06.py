print("Escreva alguma(s) palavra(s) e irei dizer quantas vogais há nela: ")
word = str(input()) # Recebe alguma string do usuário, e converte em string

def conta_vogais(string):
    string = string.lower() # Converte todas as letras para minúsculas
    result = {}
    vogais = 'aeiou'
    for i in vogais: # Faz uma iteração no array de vogais
        if i in string: # Faz uma iteração na string do usuário
            # Conta quantas vogais tem na string
            result[i] = string.count(i)
    return result


print(conta_vogais(word))