lista=('lapis',1.50,'Borracha',2,'Caderno',15.90,'Estojo',25,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.30
       ,'Canetas',22.30,'Livro',34.90)
print('-'*30)
print(f'{"LISTA DE ITENS":^30}')
print('-'*30)
for item in range(0,len(lista)): #lendo cada item da lista
    if item % 2 ==0 : #se o item for par ele ira apenas printar os nomes
        print(f'{lista[item]:.<30}',end='')
    elif item % 2 == 1:# se o item for impar ele ira apenar printar os precos
        print(f'R$ {lista[item]:.2f}')
