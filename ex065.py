n = soma = media = ma = me = cont = 0  # ou seja até aqui o (numero, soma, media, maior, menor) é igual a 0
continuar = 'S'  # ou seja se o usuario digitar S o programa ira continuar
while continuar != 'N':  # enquanto o N não for digitado o while ira continuar sendo executado
    cont += 1
    soma += n
    media = float(soma / cont)
    n = int(input('Digite um numero: '))  # a partir de agora o n equivale ao numero do usuario
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()  # usuario escolhe entre S ou N
    if cont == 1:  # Se o usuario digitar apenas um numero esse numero ser o maior e tambem o menor
        ma = me = n  # "ma" e "me" serão o mesmo numero digitado
    else:
        if n > ma:  # aqui o numero maior sera o "ma"
            ma = n  # "ma" sera o maior numero digitado
        if n < me:  # aqui o numero menor sera o "me"
            me = n  # "me" sera o menor numero digitado
print('voce digitou {} numeros e a media entre eles é de {:.2f}\nO maior valor foi {} e o menor valor foi {}'.format(cont,media,ma,me))
