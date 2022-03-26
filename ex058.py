from random import randint

computador = randint(0, 100)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 100.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... ')
        else:
            print('Menos... ')
print('Parabens voce acertou com {} tentativas!!! O numero que pensei foi {}'.format(palpites, computador))
