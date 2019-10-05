#Matheus Henrique
#119210656 - Ciência da Computação
#----------------------------------
#O programa verifica se o BCD é válido (imprime o resultado) ou invalido. E, caso o número tenha mais ou menos que 8 bits, o programa retorna a mensagem "Tente novamente."

print('---Conversor de BCD de 8 bits---')
print('---Para sair do programa digite, fim.---')

while True:
    binario = input('\nDigite o BCD:\n').lower()
    
    bin1 = ''
    bin2 = ''

    if binario == 'fim':
        break

    for i in range(len(binario)):
        if i<4:
            bin1 += str(binario[i])
        else:
            bin2 += str(binario[i])
    
    if len(binario) != 8:
        print('Tente novamente.')

    elif int(bin1,2) > 9 or int(bin2,2) > 9:
        print('BCD inválido.')
    else:
        bcd1 = int(bin1,2)
        bcd2 = int(bin2,2)
        print('{}{}'.format(bcd1,bcd2))
