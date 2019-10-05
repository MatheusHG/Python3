#Matheus Henrique Guedes de Oliveira
#119210656
#-------------------------------------
#Fundo de Investimento - Unidade 5
# Programa que gerencia operações em um fundo de investimento. Nesse fundo de investimento simplificado, 
#novas contribuções serã o aceitas desde que a quantia passada não seja menor que a média dos valores já investidos. 
#O programa ler da entrada padrão uma sequência de valores a serem incluídos no fundo de investimento. 
#Caso seja lida uma quantia que não obedece as regras acima, seu programa deve finalizar imprimindo 
#o valor total do fundo de investimento e a média das contribuições. Obs: Não considerar a última quantia.
    
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
