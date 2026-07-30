#Author: RFG - Kasparini


# Exercício 2 - Verificador CPF


def VerificaCPF():
    #Entrada do número de CPF   
    cpf = input("Entre com o CPF:")
    #Variáveis de apoio
    k = 1
    n = 1
    cpf_ver = 0
    cpf_ver1 = 0
    #Verificando a consistência de entrada
    try:
        int(cpf) #verifica se é inteiro
    except:
        print("* * * Erro * * * CPF digitado não é numérico")        
    else:
        if len(cpf) == 11: #verifica se tem 11 dígitos
            cpf1 = int(cpf) #transforma em inteiro criando variável de apoio
            cpf2 = int(cpf)
            l = str(cpf1) #cria uma variável de apoio transformando o int(cpf) em str 
            l = len(l) #da valor a variável l com o tamanho do cpf (facilita em caso de cpf que começa com zero)
            while k < cpf1: #descobre a potência do número
                k = k * 10
            k = k // 10
            while cpf1 > 100: #rotina que vai separando os dígitos do cpf
                digito = cpf1 // k
                cpf1 = cpf1 % k
                k = k // 10
                cpf_ver = cpf_ver + digito*(l-n) #variável que acumula a soma dos dígitos
                n = n + 1
            d10 = cpf_ver % 11 #calcula o digito verificador 10
            if d10 < 2: d10 = 0
            else: d10 = 11 - d10
            #reinicia as variáveis de apoio k e n
            k = 1
            n = 1
            while k < cpf2:
                k = k * 10
            k = k // 10
            while cpf2 > 10: #rotina para calcular o digito 11
                digito = cpf2 // k
                cpf2 = cpf2 % k
                k = k // 10
                cpf_ver1 = cpf_ver1 + digito*(l+1-n)
                n = n + 1
            d11 = cpf_ver1 % 11 #calcula o digito 11
            if d11 < 2: d11 = 0
            else: d11 = 11 - d11
            d110 = d10*10 + d11
            if d110 == cpf1: #compara os dois ultimos digitos do cpf dado, com os digitos calculados na rotina de verificação
                print("CPF válido")
            else:
                print("CPF inválido")
        else:
            print("CPF deve ter 11 digitos")
        
                
    
while True:
    VerificaCPF()


