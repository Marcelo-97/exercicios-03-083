somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheridade=0
for pessoa in range(1, 5):
    print('----- {}ª PESSOA ------'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip()).upper()
    somaidade += idade
    if pessoa == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        mulheridade+=1


mediaidade = int(somaidade / 4)
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos de idade'.format(mulheridade))
