from random import randint

v = 0  # vitoria criada
while True:
    comp = randint(0, 10)  # randomizar a escolha do computador
    num = int(input('Digite um numero: '))  # jogador escolhe o numero
    soma = comp + num  # soma entre numero do jogador e o computador
    escolha = ' '
    while escolha not in 'PI':  # enquanto o usuario nao digitar "i" ou "p" nao ira prosseguir
        escolha = str(input('Par ou Impar? [P/I]')).strip().upper()[0]  # jogador escolhe entre par ou impar
    print(f'Você jogou {num} e o computador {comp}. Total de {soma} ',end='')  # resultado do jogo
    print('DEU PAR !!!' if soma % 2 == 0 else 'DEU IMPAR !!!')
    if escolha == 'P':  # escolher igual a par "P"
        if soma % 2 == 0:  # soma dividida e se o resto for 0
            print('você Venceu!!!')
            v += 1  # contador de vitorias
        else:
            print('Voce Perdeu.')
            break  # "break" se o jogador errar
    elif escolha == 'I':
        if soma % 2 == 1:  # soma dividida e se o resto for 1
            print('Você Venceu!!!')
            v += 1
        else:
            print('Voce Perdeu.')
            break  # "break" se o jogador errar
    print('Vamos jogar novamente...')  # VOLTA PARA A LINHA 8
print(f'GAME OVER! Você venceu {v} vezes')
