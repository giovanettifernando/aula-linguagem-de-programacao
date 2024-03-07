'''
Pares entre Cinco Números

Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

Exemplo de Entrada
7
-5
6
-4
12

Exemplo de Saída
3 valores pares
'''

parCont = 0
num1 = int(input())
if num1 % 2 == 0:
    parCont += 1
else:
    parCont += 0

num2 = int(input())
if num2 % 2 == 0:
    parCont += 1
else:
    parCont += 0

num3 = int(input())
if num3 % 2 == 0:
    parCont += 1
else:
    parCont += 0

num4 = int(input())
if num4 % 2 == 0:
    parCont += 1
else:
    parCont += 0

num5 = int(input())
if num5 % 2 == 0:
    parCont += 1
else:
    parCont += 0


if parCont == 1:
    print(parCont, 'valor par')
else:
    print(parCont, 'valores pares')


