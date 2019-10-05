#Matheus Henrique Guedes de Oliveira
#119210656 - Ciência da Computação
#-----------------------------------
#Porta Eletrônica - Unidade 5
# Numa empresa, cada funcionário é identificado por um código composto de uma letra maiúscula seguida por 5 dígitos. 
#Um exemplo seria o código A12345. Funcionários da mesma categoria são identificados pelo caractere inicial do código. 
#Ou seja, A12345 pertence à categoria A.
#O programa simula um terminal de controle de ponto dos funcionários desta empresa. O registro é feito através das linhas 
#que começam com o caractere R seguidas do código do funcionário. Exemplo: "R A12345". A pesquisa, por outro lado, é marcada 
#por uma linha que começa com o caractere P seguido da letra que representa esta categoria. Exemplo: "P A".
#Assim, sempre que houver uma consulta (exemplo: "P A"), deverá imprimir na tela a quantidade de registros de pontos de funcionários 
#daquela categoria. E um funcionário pode registrar mais de uma vez o ponto.

lista_de_registro = []
print('---Registro de ponto da Empresa---')
print()
print('Digite R para registrar')
print('Digite P para contabilizar os registros da categoria')
print('Digite S para sair do programa')
print()
print('---Digite o registro---')
while True:
    cont = 0
    registro = input().upper()

    if registro[0] == 'S':
        break
    elif registro[0] == 'R':
        lista_de_registro.append(registro)
    elif registro[0] == 'P':
        for i in range(len(lista_de_registro)):
            if lista_de_registro[i][2] == registro[2]:
                cont += 1
        print(cont)
