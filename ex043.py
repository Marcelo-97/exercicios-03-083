peso= float(input('Qual é o seu peso? (Kg) '))
altura = float(input('QUal é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('voce esta ABAIXO DO PESO NORMAL')
elif 18.5<= imc <25:
    print('PARABENS, voce esta na faixa de PESO NORMAL')
elif 25<=imc<30:
    print(' voce esta em SOBREPESO')
elif 30<= imc < 40:
    print('voce esta em OBESIDADE!')
else:
    print('voce esta em OBESIDADE MORBIDA, CUIDADO!')