real = float(input('quanto dinheiro você tem? R$ '))
dolar = real / 5.11
euro = real / 6.04
rublo= real/0.07
iene=real /0.05
print('Com R${:.2f} você pode comprar:\nUS$ {:.2f}\n€ {:.2f}\nRUB {:.2f}\n¥ {:.2f}'.format(real, dolar, euro,rublo,iene))
print('Cotação feita no dia: 15/07/2021')