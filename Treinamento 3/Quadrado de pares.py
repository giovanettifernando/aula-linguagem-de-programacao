'''
Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

Entrada
A entrada contém um valor inteiro N (5 < N < 2000).

Saída
Imprima o quadrado de cada um dos valores pares, de 1 até N, conforme o exemplo abaixo.

Tome cuidado! Algumas linguagens tem por padrão apresentarem como saída 1e+006 ao invés de 1000000 o que ocasionará resposta errada. Neste caso, configure a precisão adequadamente para que isso não ocorra.

Exemplo de Entrada
6

Exemplo de Saída	
2^2 = 4
4^2 = 16
6^2 = 36
'''

N = int(input())
contador = 2


while contador <= N:
    #saida
    conta = contador**2
    print(f'{contador}^2 = {conta}')
    contador += 2 
    

