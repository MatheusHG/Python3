#Matheus Henrique
#119210656 - Ciência da Computação/UFCG
#Valor das Vendas
#----------------

def quebra_linhas(dados):
    string = '' 

    for i in range(len(dados)):
        if dados[i] == ',':
            if string == '':
                continue
            lista.append(string)
            string = ''
        elif dados[i] == ' ':
            if string == '':
                continue
            lista.append(string)
            string = ''
        else:
            string += dados[i]

    if string != '':
        lista.append(string)

def calcula_vendas(dados):
    global lista
    
    quebra_linhas(dados)

    lucro_total = float(lista[0]) + (float(lista[0])*float(lista[1]) + float(lista[0])*float(lista[2]) + float(lista[0])*float(lista[3]))

    print('O valor de venda para este produto deve ser R$ {:.2f}'.format(lucro_total))

while True:
    lista = []
    dados = input()
    if dados == '-':
        break
    else:
        calcula_vendas(dados)
