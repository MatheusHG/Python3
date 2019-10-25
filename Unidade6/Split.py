#Matheus Henrique Guedes
#119210656 - Ciência da Computação/UFCG
#--------------------------------------
#Questão do TST - Função Split

def split(string,delimitador):
    nome = ''
    lista = []
    for i in range(len(string)):
        if string[i] == delimitador:
            if nome != '':
                lista.append(nome)
                nome = ''
            else:
                continue
    
        else:
            nome += string[i]
    if nome != '':
        lista.append(nome)
    return lista

assert split('um exemplo', ' ') == ['um','exemplo']
assert split('testando', 'a') == ['test', 'ndo']
