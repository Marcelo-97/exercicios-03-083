n = cont = s = 0  # numero, soma, cont igual a 0
while True:  # laço infinito
    n = int(input('Digite um valor (999 para parar): '))  # usuario digita um numero
    if n == 999:  # se for digitado 999 o break sera executado
        break
    s += n  # apenas o que foi digitado antes do "if" sera somado TEM QUE SER APÓS O BREAK
    cont += 1  # aqui o flag não é contado TEM QUE SER APÓS O BREAK
print(f'A soma dos {cont} valores foi {s}.')
