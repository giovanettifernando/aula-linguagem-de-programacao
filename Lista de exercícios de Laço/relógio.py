'''
Crie um relógio com horas, minutos e segundos e que recomece assim que atingir as 24h
'''

from time import sleep
#da biblioteca só a função sleep. Se nao, no codigo eu colocaria time.sleep(1)

def relogio():
    while True:
        #garante que vai ser um looping infinito
        h = 0
        while h < 24:
            m = 0
            while m < 60:
                s = 0
                while s < 60:
                    print(f'{h:02}:{m:02}:{s:02}')
                    s += 1
                    #sleep(1)
                m += 1
            h += 1
