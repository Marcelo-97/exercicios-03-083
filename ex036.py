casa = float(input('Valor da casa: R$ '))
salario = float(input('qual o salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestaçao = casa / (anos * 12)
minimo = (30 * salario) / 100
print('para pagar uma casa de R${:.2f} em {}'.format(casa, anos), end='')
print('a prestação sera de R${:.2f}'.format(prestaçao))
if prestaçao >= minimo:
    print('emprestimo pode ser concedido')
else:
    print('emprestimo negado')
