'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

https://resources.beecrowd.com/gallery/images/problems/UOJ_1049_b.png

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.

Exemplos de Entrada
vertebrado
mamifero
onivoro

Exemplos de Saída
homem

'''

tipo1 = input()
tipo2 = input()
tipo3 = input()

if tipo1 == 'vertebrado':
    if tipo2 == 'ave':
        if tipo3 == 'carnivoro':
            print('aguia')
        elif tipo3 == 'onivoro':
            print('pomba')
    elif tipo2 == 'mamifero':
        if tipo3 == 'onivoro':
            print('homem')
        elif tipo3 == 'herbivoro':
            print('vaca')
elif tipo1 == 'invertebrado':
    if tipo2 == 'inseto':
        if tipo3 == 'hematofago':
            print('pulga')
        elif tipo3 == 'herbivoro':
            print('lagarta')
    elif tipo2 == 'anelideo':
        if tipo3 == 'hematofago':
            print('sanguessuga')
        elif tipo3 == 'onivoro':
            print('minhoca')


