#Author_RFG_Kasparini
#Exercício 3 - Cálculo de funções por séries de Taylor

import math

def exp2(): 
    
    
    while True:   #Início do looping de consistência

        x = input("Entre com valor de x:") or x         #Entrada de nova variável ou apenas manter a atual (ENTER)
        epi = input("Entre com valor de eps:") or epi   #Entrada de nova variável ou apenas manter a atual (ENTER)

        try:
            x = float(x)       #consistência se x é float
        except:
                print("* * * ERRO * * * Valor de x não é numérico")
                continue                    
        else:
            if x < -10 or x > 10:  #consistência para x estar entre -10 e 10
                print("* * * ERRO * * * Valor de x tem que estar no intervalo entre -10 e 10")
                continue

        try:                
            epi = float(epi)   #consistência para eps ser float
        except:
            print("* * * Erro * * * Valor de eps não é numérico")
            continue
        if epi >= 1 or epi < 0:
            print("* * * ERRO * * * Valor de eps deve estar entre 0 < eps < 1")
            continue                   
        
        else:    #carregando variáveis de apoio
            eps = 1.0
            k = 1
            n = 1
            i = x
        while abs(i/k) >= epi:   #looping para cálculo da soma da série de Taylor
            eps += i/k
            i = i*x
            n = n + 1
            k = n * k
            
            
        exp = math.exp(x)        #cálculo do epsilon através da função math dentro do Python
        dif = exp - eps          #cálculo da precisão entre a soma da série de Taylor e da função math.exp
        print("\nValores calculados para:")
        print("x =", x)
        print("eps =",epi)
        print("\nExponencial:")
        print("Usando a função math.exp  - Valor calculado: ",exp)
        print("Usando a soma de termos   - Valor calculado: ",eps,"- |Diferença|:",abs(dif))
        print("\n* * * * * * * * * *")
        y = str(input("\nDeseja realizar novo cálculo (s/n)?"))   #verifica se o usuário quer realizar novo cálculo
        if y == 's':
            continue
        break
exp2()
