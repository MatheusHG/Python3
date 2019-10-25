#Matheus Henrique Guedes
#119210656 - Ciência da Computação/UFCG
#Questão TST - Caixa Alta
#---------------------------------------
#Retorna a primeira letra maiúscula de uma frase, exceto se ela possuir apenas uma letra

def caixa_alta(x):
    frase = list(x)
    frase.insert(0, ' ')
    frase.insert(len(x)+1, ' ')
    lista = []

    for i in range(1,len(frase)-1):
        if frase[i-1] == ' ' and frase[i+1] == ' ':
            frase[i] = frase[i].lower()
            lista.append(frase[i])
            continue
        elif frase[i-1] == ' ':
            frase[i] = frase[i].upper()
            lista.append(frase[i])
            continue
        lista.append(frase[i])

    string = ''.join(lista)
    return string

assert caixa_alta("A primeira letra de cada palavra") == "a Primeira Letra De Cada Palavra"
