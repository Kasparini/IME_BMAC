# Author - RFG - Kasparini
# Exercício Programa 1 - Dispensador de notas com opções
        

def main():
    #Inicializa as variáveis que acumularão a quantidade de notas de cada valor
    cont_10 = 0
    cont_20 = 0
    cont_50 = 0
    cont_100 = 0
    while True:  
        while True: #Looping para avaliar a consistência do número de entrada (inteiro e múltiplo de 10)
            try:
                valor = int(input("Entre com o valor em reais:"))
            except:
                print("* * * Erro * * * Valor digitado não é numérico")        
            else:
                if valor > 0 and valor % 10 == 0:
                    print("Entrada válida")
                    break
                else: 
                    if valor <= 0: #Finaliza o programa para valor de entrada ser menor ou igual a zero
                        print("*** Fim da Operação ***")
                        print("Total de notas sacadas:")
                        print(cont_100, "nota(s) de 100") #Imprime a soma das notas de 100
                        print(cont_50, "nota(s) de 50") #Imprime a soma das notas de 50
                        print(cont_20, "nota(s) de 20") #Imprime a soma das notas de 20
                        print(cont_10, "nota(s) de 10") #Imprime a soma das notas de 10
                        soma = cont_100*100 + cont_50*50 + cont_20*20 + cont_10*10 #Soma o total sacado em reais
                        print("Valor total:", soma, "Reais")
                        quit() #Termina o programa
                    else: print("* * * Erro * * * Valor tem que ser multiplo de 10")
        #Sendo aceito o valor de entrada, inicia o estudo do valor em termos de quantidade de notas de cada valor, como primeira opção
        n_100 = valor // 100
        s_100 = valor % 100
        n_50 = s_100 // 50
        s_50 = s_100 % 50
        n_20 = s_50 // 20
        s_20 = s_50 % 20
        n_10 = s_20 // 10
        print("Quantidade de notas a serem sacadas:") #Imprime a primeira opção para saque
        if n_100 != 0:
            print(n_100, "nota(s) de 100")
        if n_50 != 0:
            print(n_50, "nota(s) de 50")
        if n_20 != 0:
            print(n_20, "nota(s) de 20")
        if n_10 != 0:
            print(n_10, "nota(s) de 10")
        y = str(input("Deseja sacar desta forma (s/n)?")) #Questiona se aceita sacar nessa opção
        if y == 's':
            #Contador para acumular quantidade de notas
            cont_100 = n_100 + cont_100
            cont_50 = n_50 + cont_50
            cont_20 = n_20 + cont_20
            cont_10 = n_10 + cont_10
            print("* Confirmado *")
        else:
            if y == 'n':
                n_50 = valor // 50
                s_50 = valor % 50
                n_20 = s_50 // 20
                s_20 = s_50 % 20
                n_10 = s_20 // 10
                #Imprime a segunda opção para saque
                if n_50 != 0:
                    print(n_50, "nota(s) de 50")
                if n_20 != 0:
                    print(n_20, "nota(s) de 20")
                if n_10 != 0:
                    print(n_10, "nota(s) de 10")
                y = str(input("Deseja sacar desta forma (s/n)?"))
                if y == 's':
                    #Contador para acumular quantidades de notas
                    cont_50 = n_50 + cont_50
                    cont_20 = n_20 + cont_20
                    cont_10 = n_10 + cont_10
                    print("* Confirmado *")
                else:
                    if y == 'n':
                        n_20 = valor // 20
                        s_20 = valor % 20
                        n_10 = s_20 // 10
                        #Imprime a terceira opção para saque
                        if n_20 != 0:
                            print(n_20, "nota(s) de 20")
                        if n_10 != 0:
                            print(n_10, "nota(s) de 10")
                        y = str(input("Deseja sacar desta forma (s/n)?"))
                        if y == 's':
                            #Contador para acumular quantidades de notas
                            cont_20 = n_20 + cont_20
                            cont_10 = n_10 + cont_10
                            print("* Confirmado *")
                        else:
                            if y == 'n':
                                n_10 = valor // 10
                                #Imprime a quarta opção para saque
                                if n_20 != 0:
                                    print(n_10, "nota(s) de 10")
                                y = str(input("Deseja sacar desta forma (s/n)?"))                   
                                if y == 's':
                                    #Contador para acumular quantidades de notas
                                    cont_10 = n_10 + cont_10
                                    print("* Confirmado *")
                                else:
                                    if y == 'n':
                                        print("* Nenhuma opção foi aceita *")
                                        continue
                                    else:
                                        print("* Entrada inválida *")          
                            else:
                                print("* Entrada inválida *") 
                    else: 
                        print("* Entrada inválida *")           
            else:
                print("* Entrada inválida *")
                continue
        continue

main()

    

