totalcom=maismil=maisbar=cont=barato=0 # as variaveis criadas aqui são "total de compras" , "mais de mil" , "mais barato","contador","barato"
print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-'*30)
while True:
    produto=str(input('Nome do produto: ')).strip() # usuario digita um produto
    preço=float(input('Preço: R$ ')) # preço do produto
    cont+=1
    totalcom+=preço # soma do total de compras ==0 mais o "preço" == ao primeiro numero digitado
    if preço >= 1000:
        maismil+=1
    if cont == 1 or preço < maisbar: # se o "contador" for ==1 ou "preço" for menor que "maisbar"
        maisbar = preço # "maisbar se torna o "preço"
        barato = produto  # "barato" se torna o "produto"
    resp=' ' # continuar a listar mais produtos
    while resp not in 'SN': # enquanto o usuario nao digitar S ou N nao ira continuar
        resp=str(input('Quer continuar? [S/N]').strip().upper()[0]) # S ou N para continuar
    if resp == 'N':
        break
print('-'*30)
print(f'O total da compra foi de R$ {totalcom:.2f}')
print(f'Temos {maismil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa {maisbar:.2f}')

