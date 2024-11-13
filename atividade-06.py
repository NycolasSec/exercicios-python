print("Escreva alguma(s) palavra(s) e irei dizer quantas vogais há nela: ")
word = str(input())

def conta_vogais(string):
    string = string.lower()
    result = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in string:
            result[i] = string.count(i)
    return result


print(conta_vogais(word))