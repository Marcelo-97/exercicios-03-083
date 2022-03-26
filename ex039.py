from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Voce tem que se alistar imediatamente')
elif idade < 18:
    saldo = idade - 18
    print('ainda falta {} para voce se alistar'.format(saldo))
    ano = atual + saldo
    print('seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('voce ja deveria ter se alistado ha {} anos'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {} ano'.format(ano))
