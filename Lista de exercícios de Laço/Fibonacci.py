'''
A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, ... Escreva um
programa que apresente a série de Fibonacci até o n-ésimo termo (n > 0).
'''

n = int(input('Digite o número de termos da sequência de Fibonacci que você deseja calcular: '))
cont = 0
ant = 0
atual = 1

while cont < n:
    print(atual)
    prox = ant + atual
    ant = atual
    atual = prox
    cont += 1
   


    

