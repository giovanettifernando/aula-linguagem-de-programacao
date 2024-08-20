'''
Conversão de polegadas

Megan quer comprar um novíssimo smartphone e está muito empolgada com as possibilidades que uma tela de várias polegadas pode oferecer para seu entretenimento. Mas há um problema, Megan percebeu que não sabe lidar com polegadas, afinal sempre realizou cálculos usando centímetros e gostaria de se basear nessa unidade de medida para imaginar o tamanho da tela de seu futuro smartphone. Você pode ajudar Megan?

Seu trabalho é construir um programa que receba como entrada um número real, simbolizando uma quantidade de polegadas, e exiba o equivalente em centímetros. Lembre-se que uma polegada equivale a 2,54 cm.

Entrada

Um número real representando uma quantidade de polegadas.

Saída

Um número real, com exatamente três casas decimais, representando a conversão da quantidade de polegadas da entrada na respectiva quantidade em centímetros.

Samples Input
10.0

Samples Output
25.400
'''

num = float(input())

print(f'{num*2.54:.3f}') 
