
# Author: RFG - Kasparini
# Exercicio 4 - Histograma


import numpy as np
from random import seed, randrange
# Gera n números aleatórios no intervalo [a, b)


def GeraAmostra(a, b, n):
    # Use o seu NUSP como semente
    
    NUSP = 3660211
    seed(NUSP)
    amostra = n * [0]
    for k in range(n):
        amostra[k] = a + float(randrange(1000000)) * (b - a)/1000000.0
    return amostra

def histograma(a, b, n):
    
    while True:
        i = input("\nEntre com o número de intervalos:")
        try: i = int(i)
        except: 
            print("\n* * * ERRO * * * Valor de i precisa ser inteiro")
            continue
        else:
            print("\nIntervalo", f'{"Frequência":>20}', f'{"Gráfico":>10}')
        while True:
            h = abs(((b)-(a))/i)
            round(h)
            x = a
            count = 0
            y = 0
            k = a
            t = len(amostra) - 1
            while x < b:
                k += h
                #print(k)
                
                while amostra[y] < k:  
                    if y == t:
                        print("%+4.4f" %x, "à", "%+4.4f" %k, "%8d" %count, "%6s" %" " ,(int(count) * "\u2592"))
                        return
                    else:
                        count += 1
                        y += 1     
                #round(k)
                #round(x)   
                print("%+4.4f" %x, "à", "%+4.4f" %k, "%8d" %count, "%6s" %" " ,(int(count) * "\u2592"))
                x += h
                count = 0
            continue            
        

while True:
    print("\nEntre com o intervalo:") 
    a = input("Limite inferior:")
    b = input("Limite superior:")
    n = input("\nEntre com a quantidade de elementos da amostra:")
    try:
        a = float(a)    #Avalia se a é float
        b = float(b)       #Avalia se b é float   
    except:
        print("\n* * * ERRO * * * Valor de a não é numérico")
        continue                    
    else:
        if a > b : #Avalia se a é menor que b
            print("\n* * * ERRO * * * Valor de a é maior que b, entre novamente com o intervalo")
            continue
        else:
            try: n = int(n)
            except:
                print("\n* * * ERRO * * * Valor de n tem que ser inteiro")
            else:   
                break

am = GeraAmostra(a, b, n)
for k in range(n):
    if k % 10 == 9: print("%10.5f" %am[k])
    else: print("%10.5f" %am[k], end = ' ')
amostra = am
amostra.sort()

while True: histograma(a,b,n)
