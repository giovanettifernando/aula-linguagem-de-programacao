'''
Crie um programa que peça letras como entrada, uma por vez, até que seja lida a letra
'x', ao final, o programa deve exibir a quantidade de letras lidas sem contabilizar 'x'.
Observação: lembre-se que o Python diferencia maiúsculas e minúsculas.
'''

letra = input()
qtd = 0

while letra != 'x':
    if ord(letra) > ord('x'):
        print('A letra digitada está depois de x.')
        break
    else:
        qtd += 1
        letra = chr(ord(letra) + 1)
        
if qtd > 0:
    print(qtd)

                     
