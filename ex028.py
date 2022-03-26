import random
import time
computador=random.randint(0,5)
print('-=-'*10)
print('estou pensando em um numero...')
print('-=-'*10)
numero=int(input('em que numero eu pensei? '))
print('processando...')
time.sleep(2)
if numero == computador:
    print('Parabens voce acertou!!!')
else:
    print('voce errou, SEU MERDA! eu pensei em {} e não no {}'.format(computador,numero))







