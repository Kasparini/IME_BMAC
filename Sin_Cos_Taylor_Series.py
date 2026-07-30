#Author: RFG - Kasparini
#Exercício Programa 2 - Cálculo de funções por séries de Taylor - Seno e Cosseno

import math
from time import process_time


def main():
    #Função principal, ela chamará as funções Seno() e Cosseno() quando necessário

    while True: #Looping para avaliar a consistência das entradas (float, int, x dentro de 0 a 2pi, etc)
           
        x = input("\nEntre com valor de x:") or x #verifica se o usuário quer entrar com nova variável ou se utiliza a existente (apenas pressinando ENTER)
        n = input("Entre com valor de n:") or n
        
        try:
            x = float(x)    #Avalia se x é float   
        except:
                print("* * * ERRO * * * Valor de x não é numérico")
                continue                    
        else:
            if x > 2*(math.pi): #Avalia o tamanho de x
                x = x%(2*(math.pi)) #Converte o x para dentro de um ciclo (0 a 2pi)
        try:                
            n = int(n)       #Avalia de n é inteiro
        except:
            print("* * * Erro * * * Valor de n inválido, entre com um número inteiro")
            continue                   
        else:
            if n > 50: #Avalia se n é maior que 100 (limite de 50 termos conf. revisáo do prof. dia 07/07)
                print("* * * ERRO * * * Valor de n tem que ser menor ou igual a 50")
                continue
            if n < 0:  #Avalia entrada negativa para n
                print("* * * ERRO * * * Valor de n não pode ser menor que zero")
                continue   

        #Início do trecho do programa onde rodará o cálculo do Seno e Cosseno, comparando a função da biblioteca math e a soma de termos 
        o = process_time()         #Grava o valor atual do relógio na variável 'o'
        seno(x, n)                 #Calcula o Seno pela soma de termos (Série de Taylor)    
        dts = process_time() - o   #Calcula o tempo transcorrido no cálculo e grava na variável dts
        
        o = process_time()         #Grava o valor atual do relógio na variável 'o'
        cosseno(x, n)              #Calcula o Cosseno pela soma de termos (Série de Taylor)
        dtc = process_time() - o   #Calcula o tempo transcorrido no cálculo e grava na variável dtc

        p = process_time()
        exp = math.sin(x)           #Calcula o Seno através da biblioteca math do Python
        dps = process_time() - p    #Grava o tempo transcorrido no processo em dps

        p = process_time()
        esp = math.cos(x)           #Calcula o Cosseno através da biblioteca math do Python
        dpc = process_time() - p    #Grava o tempo transcorrido no processo em dpc
        
        print("\nValores calculados para:")
        print("x =", x)
        print("n =", n)
        print("\nSeno:")
        print("Usando a função math.sin  - Valor calculado: ",exp, f'{" - tempo:":>10}', dps)
        print("Usando a soma de termos   - Valor calculado: ",seno(x,n), f'{" - tempo:":>10}',dts)
        print("\nCosseno:")
        print("Usando a função math.cos  - Valor calculado: ",esp, f'{" - tempo:":>10}',dpc)
        print("Usando a soma de termos   - Valor calculado: ",cosseno(x,n), f'{" - tempo:":>10}',dtc)
        print("\n* * * * * * * * * *")

        y = str(input("\nDeseja realizar novo cálculo (s/n)?")) #Verifica se o usuário quer realizar novo cálculo
        if y == 's':
            continue
        else:
            break
    
def seno(x, n): #Função Seno, cálculo através da soma de termos (Série de Taylor)
    
    #Carrega variáveis de apoio
    sen = x
    k = 6
    e = 3
    c = -1
    t = -1
    z = x*x
    s = x*x*x
            
    for i in range (1, n, 1):   #Looping que realiza a soma
        sen += t * (s/k)
        t = t*c
        s = s*z
        k = k*(e+2)*(e+1)
        e = e + 2
    return sen
    
 
def cosseno(x, n): #Função Cosseno, cálculo através da soma de termos (Série de Taylor)

    #Carrega variáveis de apoio      
    cos = 1
    c = -1
    t = -1
    z = x*x
    h = 2
    y = x*x
    a = 2
    
    for i in range (1, n, 1):   #Looping que realiza a soma
        cos += t * (y/h)
        t = t*c
        y = y*z
        h = h*(a+2)*(a+1)
        a = a + 2
    return cos  


   
main()
