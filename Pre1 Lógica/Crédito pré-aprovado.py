'''
Suponha que você criará um programa para um banco que receberá como entrada um nome de um cliente, a idade do cliente e a renda mensal do cliente. O programa deverá exibir como saída o valor máximo que esse cliente poderá receber de empréstimo de acordo com esses critérios:
'''
nomeCliente = input('Olá, qual o seu nome? ')
idadeCliente = int(input(f'Muito prazer, {nomeCliente}. Me diga: qual a sua idade? '))
salarioCliente = float(input(f'{nomeCliente}, agora digite aqui seu salário para avaliação de crédito: '))

if idadeCliente <=25:
        print(f'{nomeCliente}, temos um crédito pré-aprovado para você no valor de R$ {salarioCliente*0.5:.2f}')
elif idadeCliente > 26 and idadeCliente <= 35:
    print(f'{nomeCliente}, temos um crédito pré-aprovado para você no valor de R$ {salarioCliente*0.75:.2f}')
elif idadeCliente > 36 and idadeCliente <= 45:
    print(f'{nomeCliente}, temos um crédito pré-aprovado para você no valor de R$ {salarioCliente:.2f}')
else:
    print(f'{nomeCliente}, favor contatar seu gerente')
                       
