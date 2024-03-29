credito = float(input('Digite o valor do seu crédito: '))
total = 0
contador = 1

while True:
    precoItem = float(input(f'Digite o preço do item {contador}: '))
    if precoItem > credito:
        print(f'Compra do item {contador} negada!')
        break
    credito -= precoItem
    total += precoItem
    contador += 1

print(f'\nSeu crédito restante: R$ {credito:.2f}')
print(f'Itens comprados: {contador - 1}')
print(f'Total da compra: R$ {total:.2f}')



