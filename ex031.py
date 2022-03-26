viagem = float(input('Qual é a distancia da sua viagem? '))
#curta=viagem*0.50
#longa=viagem*0.45
print('voce esta prestes a começar uma viagem de {:.2f}Km'.format(viagem))
if viagem<=200:
    preço=viagem*0.50
else:
    preço=viagem*0.45
print('E o preço da sua passagem sera de R${:.2f}'.format(preço))
'''if viagem <=200:
    print('E o preço da sua passagem sera de R${:.2f}'.format(curta))
else:
    print('E o preço da sua passagem sera de R${:.2f}'.format(longa))'''


