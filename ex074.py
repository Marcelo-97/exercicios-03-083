from random import randint  # importo random

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))  # randomizo cada numero
print('os valores sorteados foram:', end=' ')
for x in num: # cada vez que o "x" for printado um numero diferente irá aparecer
    print('{} '.format(x), end='')
print(f'\nO maior numero sortado foi {max(num)}') #maior numero
print(f'O menor numero sortado foi {min(num)}')#menor numero
