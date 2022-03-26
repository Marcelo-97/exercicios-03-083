n = cont = 0  # "n"==numero que o usuario quer multiplicar "cont" contador de 1 a 10
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))  # peço ao usuario qual numero ele quer
    if n < 0:  # se o usuario digitar um numero menor que 0 o "break" ira acontecer TEM QUE SER APOS O INPUT
        break
    print('-' * 30)
    for cont in range(1, 11):  # aqui sera contado de 1 a 10
        print(f'{n} X {cont} = {n * cont}')  # aqui sera multiplicado de 1 a 10
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
