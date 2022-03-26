import random
n1=str(input('primeiro troxa: '))
n2=str(input('segundo troxa: '))
n3=str(input('terceiro troxa: '))
n4=str(input('quarto troxa: '))
n5=str(input('quinto troxa: '))
lista=[n1,n2,n3,n4,n5]
escolhido=random.choice(lista)
print('O maior troxa dos troxas escolhido foi {}'.format(escolhido))
