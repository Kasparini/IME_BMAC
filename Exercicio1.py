#Ricardo Ferreira Gasparini - NUSP 3660211
#Exercício 1 - Sequência Fibonacce


N = int(input("Entre com o valor de N:"))

a0 = 0
a1 = 1

print("Sequência de Fibonacci - menores ou iguais a", N, ":")

while a1 <= N:
    an = a1
    fibo = an
    a1 = a1 + a0
    a0 = an
    print(fibo)
