from datetime import date

atual = date.today().year
nascimento = int(input('ano de nascimento '))
idade = atual - nascimento
print('o atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('classificaçao: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificaçao: MASTER')
