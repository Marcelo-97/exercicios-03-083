salario = float(input('Qual o salário do funcionário? R$ '))
if salario >= 1250.00:
    novo = (salario * 10) / 100
    aumento = novo + salario
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, aumento))
else:
    salario <= 1250.00
    novo = (salario * 15) / 100
    aumento = novo + salario
    print('Quem ganhava R$ {:.2f} passa a ganher R$ {:.2f} agora.'.format(salario, aumento))
