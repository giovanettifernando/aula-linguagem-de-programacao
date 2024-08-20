def valores():
    for i in range (9):
        entrada = int(input())
        lista.append(entrada)    
    return

lista = []
valores()
lista_ordenada = sorted(lista)

print(lista)
print(lista_ordenada[0])


    
