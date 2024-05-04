'''
Desenhar um fluxograma em que dado a quantidade de alunos de uma turma, calcular a
média semestral de cada aluno, a média geral da turma e mostrar uma mensagem para os
alunos aprovados.
'''

alunos = int(input('Digite a quantidade de alunos na sala: '))
contador = 1
acumulador = 0

while contador <= alunos:
    nota1 = float(input(f'Nota 1 do aluno {contador}: '))
    nota2 = float(input(f'Nota 2 do aluno {contador}: '))
    nota3 = float(input(f'Nota 3 do aluno {contador}: '))
    media = (nota1 + nota2 + nota3) / 3
    print(f'A media do aluno {contador} é {media:.2f}')
    acumulador += media
    contador += 1


print(f'A média da classe é {(acumulador/alunos):.2f}') 
print('Obrigado e parabéns aos aprovados!')
