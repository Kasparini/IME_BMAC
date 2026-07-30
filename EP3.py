#Ricardo Ferreira Gasparini - NUSP 3660211
#Exercício Programa 3 - Palpites na Megasena 2021


from random import randrange

#Inícío do programa

print("\nLeitura do arquivo de sorteios")
print("Montagem da tabela de último sorteio de cada número")    

while True:

    file = str(input("\nEntre com o nome do arquivo:")) #Recebe o nome do arquivo dos resultados da megasena
    

    def LeiaMatriz(file):
        #Lê e retorna uma matriz contendo toda as apostas da megasena
        
        mat = []

        try:
            arq = open(file,"r")
            
        except:
            print("Erro na abertura do arquivo (open)")
            x = 1
            return 
        #ler cada uma das linhas do arquivo
        i = 0
        for linha in arq:
            try:
                lin = linha[:len(linha) - 1] #tira o \n do final
                v = lin.split('\t') #separa os elementos da string
                mat.append([]) #adiciona um linha na matriz
                #transforma strings numéricos em números inteiros
                for j in range(8):
                    if j == 1:
                        mat[i].append(v[1])
                    else:
                        mat[i].append(int(v[j]))
                i = i + 1
            except: #se tiver erro acima
                print("Erro no split(), no int() ou no append()")
                return None
        arq.close()
        return mat


    chk = [] #Gera uma matriz
    chk = LeiaMatriz(file) #Recebe a matriz lida no arquivo indicado
    try:
        len(chk) != 0 #valida entrada correta da matriz
    except:
        continue

    print("\nEscolha de apostas") 


    def escolheaposta(n): #gera um palpite aleatório, de quantidade n, entre 1 e 60
        apt = []
        for x in range(n):
            d1 = randrange(1, 61)
            while d1 in apt:
                d1 = randrange(1, 61)
            if d1 not in apt:
                apt.append(d1)
        apt.sort()
        return apt


    def Megasena(file):
        #Função principal, ela chamará a rotine de escolha do numero ideal

        while True: #Looping para avaliar a consistência da entrada
            
            n = input("\nQuantidade de números da aposta:") #recebe a quantidade de números da aposta
            
            try:
                n = int(n)    #Avalia se n é inteiro   
            except:
                    print("* * * ERRO * * * Valor de n não é numérico")
                    continue                    
            else: #avalia se a quantidade de números está entre 6 (mínimo) e 12 (máximo)
                if n < 6:
                    print("Valor inválido, quantidade de apostas deve ser entre 6 e 12 números")
                    continue
                if n > 12:
                    print("Valor inválido, quantidade máxima de aposta deve ser 12 números")
                    continue

            print("Aposta escolhida - ", n, "números:")
            qt = escolheaposta(n) # carrega a matriz 'aposta' com os números do palpite aleatório gerado
            aposta = qt
            print(aposta)
                    
            cont = 0 #cria uma varável que vai ajudar a contar os numeros repetidos por linha da matriz megasena2021
            for l in range(len(chk)): #começa um looping na linha 'l' (começa da primeira linha e vai até o comprimento total da matriz)
                for j in range(2,8): #lê os valores dos resultados da matriz megasena2021, do primeiro ao sexto número
                    for i in range(n): #lê, um por um, todos os números da aposta
                        q = chk[l][j] #pega o número do resultado
                        p = aposta[i] #pega o número da aposta
                        if q == p: #compara os dois
                            cont += 1 #se for igual, soma 1 na varável 'cont'
                if cont >= 6: #se a variável 'cont' chegar a contagem de 6 dentro de uma mesma aposta, a aposta é considerada inválida
                    print("* * * Aposta inválida")
                    print("* * * Números já sorteados no sorteio",chk[l][0], "de", chk[l][1])
                    return 
                l += 1 #vai para a segunda linha da matriz resultados megasena2021
                cont = 0 #zera o contador para a análise da nova linha
            
            print("* * * Aposta válida")
            continue


    while True: Megasena(file)

