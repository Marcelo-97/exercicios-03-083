num=int(input('Digite um numero: ')),int(input('Digite outro numero: ')),int(input('Digite mais um numero: ')),int(input('Digite o ultimo numero: '))
#pedindo ao usuario colocar cada numero dentro da tupla
print(f'Os valores que vc digitou foi {num}')   # printando todos os numeros digitados
print(f'O valor 9 foi digitado {num.count(9)} vezes') # contando quantas vezes o numero 9 foi digitado
if 3 in num: # se foi digitado um numero 3
        print(f'O valor 3 foi digitado na {num.index(3)+1}ª posição')
else: # se nao foi digitado nenhum numero 3
    print ('Não foi digitado nenhum numero 3')
print(f'Os valores pares digitados foram: ',end='')
for x in num: #para cada "x" sera dividido por 2 se o resto for igual a 0 ele sera par
    if x % 2 ==0:
        print(x, end=' ')

