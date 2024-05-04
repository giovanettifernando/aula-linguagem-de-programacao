'''
Maior e Posição
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

Exemplo de Entrada
2
113
45
34565
6
...
8

Exemplo de Saída
34565
4
'''

#primeiro exercício
'''
lista = 100 * []
i = 0

for i in range (100):
    valor = int(input())
    lista.insert(i,valor)
    i += 1

nMax = max(lista)
nPos = lista.index(nMax) + 1

print(nMax)
print (nPos)
'''

#refatorado
lista = []

for i in range(100):
    lista.append(int(input()))

nMax = max(lista)
nPos = lista.index(nMax) + 1

print(nMax)
print(nPos)
