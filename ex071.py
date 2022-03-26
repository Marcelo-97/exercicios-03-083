
print('='*30)
print('{:^30}'.format('BANCO'))
print('='*30)
valor=int(input('Que valor você quer sacar? '))    # usuario digita um "valor"
total = valor    # o "valor" se torna o "total" a retirar
ced=50    # começando pela cedula de 50 reais
totced=0    # Total de cedulas
while True:
    if total >= ced:    # se o "total" for mais ou igual a cedula
        total -= ced    # a "cedula sera subtraida para completar o valor "total"
        totced+=1    # cada vez que essa cedula for retirada sera contada mais 1
    else:
        if totced>0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:   # se a cedula for igual a 50
            ced= 20    # a variavel cedula se tornara 20 reais e nao mais sera 50
        elif ced==20:   # se a cedula for igual a 20
            ced= 10   # a variavel cedula se tornara 10 reais e nao mais sera 20
        elif ced ==10:   # se a cedula for igual a 10
            ced =1  # a variavel cedula se tornara 1 reais e nao mais sera 10
        totced=0   #toda vez que mudar a nota o total de cedulas tem que voltar a 0
        if total == 0:    # se o total for igual a 0 o break ira acontecer
            break
print('='*30)
print('Volte sempre!!')

