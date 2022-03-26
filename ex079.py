valores=[]
resp=' '
while True:
    n=(int(input('Digite um valor: '))) #usuario ira digitar o valor de "n"
    if n not in valores:
        valores.append(n)   # o valor digitado em "n" sera adicionado
        print('Valor adicionado com sucesso')
    else:              #se ja estiver ele nao sera adicionado
        print('Valor ja foi adicionado!')
    resp=str(input('Quer continuar? [S/N]: ' )).upper().strip()[0]
    while resp not in 'NS':   # enquanto o usuario nao digitar 'N' ou 'S'
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp in 'N':
        break
valores.sort()
print(f'Voce digitou os valores {valores}')
