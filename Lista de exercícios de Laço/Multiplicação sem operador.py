'''
Desenhar um fluxograma que lê dois números inteiros e calcula a multiplicação entre os
números dados, sem o uso do operador *, mas sim pela soma sucessiva de um deles.
Exemplo: 3 x 4 = 3 + 3 + 3 + 3 = 4 + 4 + 4 = 12


def fator():
    ft = float(input('Digite o valor a ser multiplicado'))
    contador = 0
    acumulador = 0
    
    while contador <= ft:
        acumulador += ft

    return acumulador
'''

def fator(num1, num2):
    resultado = 0
    contador = 0
    
    while contador < num2:
        resultado += num1
        contador += 1
    
    return resultado

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))


resultado = fator(num1, num2)
print(f'O resultado da multiplicação é: {resultado}')
