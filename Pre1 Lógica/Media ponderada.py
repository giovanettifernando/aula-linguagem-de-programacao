'''
Crie um programa que solicite ao usuário três números reais que representam três notas de provas de um aluno. Chame as notas de n1, n2 e n3. O programa deverá exibir a média ponderada do aluno considerando que n1 tem peso 2, n2 tem peso 4 e n3 tem peso 8. Exiba a média com duas casas decimais.
'''

n1 = float(input('digite o valor da primeira nota:'))
n2 = float(input('digite o valor da segunda nota:'))
n3 = float(input('digite o valor da terceira nota:'))

pesoN1 = 2.0
pesoN2 = 4.0
pesoN3 = 8.0
somaPeso = pesoN1 + pesoN2 + pesoN3

media = (n1 * pesoN1 +  n2 * pesoN2 + n3 * pesoN3) / somaPeso
print(f'media = {media:.2f}')


