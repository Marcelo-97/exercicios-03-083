cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze'
        , 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
resp='S'
while resp != 'N':
    while True:
            num = int(input('Digite um numero de 0 a 20: '))
            if 0 <= num <= 20:
                break
            else:
                print('Tente novamente.')
    print(f'Voce digitou o numero {cont[num]}')
    resp = str(input('Deseja jogar novamente? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja jogar novamente? [S/N]: ')).strip().upper()[0]
print('Fim.')






