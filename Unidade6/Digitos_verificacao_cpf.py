#Matheus Henrique Guedes 
#119210656 - Ciência da Computação/UFCG
#Questões do TST - Dígitos de Verificação do CPF

def calcula_digitos_verificacao(cpf):
    cpf_final = ''

    for i in range(2):
        novo_cpf = ''
        soma = 0
        for i in range(len(cpf)-1,-1,-1):
            novo_cpf += cpf[i]
        for i in range(len(novo_cpf)):
            soma += int(novo_cpf[i])*(i+2)
    
        x = (10*(soma))%11
        if x == 10:
            x = 0

        cpf = cpf + str(x)    
        cpf_final += str(x)

    return cpf_final

assert calcula_digitos_verificacao('153245875') == '40'
