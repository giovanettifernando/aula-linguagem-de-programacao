'''
Quanto tempo?

"Não tem jeito!", Julius repete para si mesmo que o trânsito da cidade grande é o maior vilão de seus dias, fazendo com que gaste muito tempo no percurso entre sua casa ao primeiro emprego, entre seu primeiro emprego ao segundo emprego, e entre seu segundo emprego até o regresso à sua casa. Pois é, Julius tem dois empregos!

Julius é ótimo na realização de contas, mas como está sempre com pressa, nunca teve tempo para calcular o tempo total gasto no trânsito, desde o momento que sai de casa até o momento que regressa. Seu relógio é antigo, não possibilitando cronometrar um percurso, pausar e continuar a cronometragem no próximo, por isso só sabe o tempo gasto entre os percursos isoladamente, mas não o tempo gasto nos percursos somados. Até ofereceram um novo relógio com desconto para Julius, para ele respondeu ao vendedor que "não comprar o relógio daria um desconto maior".

Você, como um bom amigo, se ofereceu para criar um programa que recebe como entrada os tempos dos três percursos de Julius (de casa ao primeiro emprego, do primeiro emprego ao segundo e do segundo à casa) e exibe o tempo total consumido. Lembre-se que os tempos serão dados em minutos!

Entrada

Três números inteiros, um por linha, representando os tempos (em minutos) gastos por Julius em seus percursos.

Saída

O tempo total gasto por Julius seguido por um espaço em branco e pela palavra "minutos", sem aspas e em minúsculo, conforme exemplos.

Samples Input
275
245
212

Samples Output
732 minutos

'''

A = int(input())
B = int(input())
C = int(input())

print(A+B+C, 'minutos')
