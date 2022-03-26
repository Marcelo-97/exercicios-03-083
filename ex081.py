valores=[]
resp=' '
while True:
    n=int(input('Digite um valor: '))
    valores.append(n)
    resp=str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp== 'N':
        break
print(f'Voce digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('Existe um numero 5 na lista!!!')
else:
    print('Não foi encontrado o numero 5 na lista!')

