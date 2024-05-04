'''
Fatorial Simples

Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada
A entrada contém um valor inteiro N (0 < N < 13).

Saída
A saída contém um valor inteiro, correspondente ao fatorial de N.

Exemplo de Entrada
4

Exemplo de Saída
24
'''

N = int(input())
acumula = 1

for i in range (N):
    ram = (N-i)
    i += 1
    acumula *= ram

print(acumula)
