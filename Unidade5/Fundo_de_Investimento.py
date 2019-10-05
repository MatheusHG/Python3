#Matheus Henrique Guedes de Oliveira
#119210656
#Fundo de Investimento - Unidade 5

quant_valor = 0
soma_valor = 0
media_total = 0

while True:
    valor = float(input())

    if valor < media_total:
        print('Saldo total do FIS: R${:.2f}.'.format(soma_valor))
        print('Média das contribuições: R${:.2f}.'.format(media_total))
        break

    quant_valor += 1
    soma_valor += valor
    media_total = (soma_valor)/quant_valor
