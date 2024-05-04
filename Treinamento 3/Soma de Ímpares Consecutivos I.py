'''
Soma de Impares Consecutivos I

Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

Exemplo de Entrada
6
-5

Exemplo de Saída
5
'''

#primeira tentativa correta
'''
X = int(input())
Y = int(input())

if X != Y:

    if X < Y:
        A = X
        B = Y
        
    if X > Y:
        A = Y
        B = X

    lista = list(range(A+1,B))

    i = 0
    acumulador = 0

    for i in lista:
        if i % 2 == 1:
            acumulador += i
        i += 1
        
    print(acumulador)

else:
    print(0)
'''

#refatorado

X = int(input())
Y = int(input())

A = min(X, Y) + 1
B = max(X, Y)

soma_impares = sum(i for i in range(A, B) if i % 2 != 0)

print(soma_impares)

