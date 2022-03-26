from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opçoes:
\33[1;37;40m[0]pedra\33[m
\33[1;30;47m[1]papel\33[m
\33[1;31;46m[2]tesoura\33[m''')
jogador = int(input('\33[1;35mQual é a sua jogada?\33[m '))
print('-='*11)
print('\33[1;31mComputador jogou {}\33[m'.format(itens[computador]))
print('\33[1;33mVocê jogou {}\33[m'.format(itens[jogador]))
print('-='*11)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('\33[1;36mDEU EMPATE!\33[m')
    elif jogador == 1:
        print('\33[1;32mVOCE GANHOU!\33[m')
    elif jogador == 2:
        print('\33[1;31mVOCE PERDEU!\33[m')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:
    if jogador == 0:
        print('\33[1;31mVOCE PERDEU!\33[m')
    elif jogador == 1:
        print('\33[1;36mDEU EMPATE!\33[m')
    elif jogador == 2:
        print('\33[1;32mVOCE GANHOU!\33[m')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2:
    if jogador == 0:
        print('\33[1;32mVOCE GANHOU!\33[m')
    elif jogador == 1:
        print('\33[1;31mVOCE PERDEU!\33[m')
    elif jogador == 2:
        print('\33[1;36mDEU EMPATE!\33[m')
    else:
        print('JOGADA INVALIDA!')
print('-='*11)
