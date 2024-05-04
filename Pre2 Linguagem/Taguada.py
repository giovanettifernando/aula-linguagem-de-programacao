'''
Tabuada

Sua tarefa é construir um programa que receba como entrada um número natural N (0 <= N <= 10) e exibir a tabuada de N de 1 até 10.

Entrada
Um número natural N (0 <= N <= 10).

Saída
Exibir a tabuada do valor dado na entrada, conforme o modelo de saída dos exemplos.

Samples Input
2

Samples Output
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
'''

n = int(input())

for i in range(1, 11):
    resultado = n * i
    print(f'{n} x {i} = {resultado}')
