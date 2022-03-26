print('{:*^40}'.format('BEM VINDO!!!'))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra sera parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total_parcelas = int(input('quantas parcelas? '))
    total = preço + (preço * 20 / 100)
    parcelas = total / total_parcelas
    print('Sua compra sera parcelada em {}x de R${:.2f}COM JUROS'.format(total_parcelas, parcelas))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
