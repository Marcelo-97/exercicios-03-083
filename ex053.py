frase = (str(input('Escreva uma frase: ')).strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso= junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('o inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print(' temos um palindromo!')
else:
    print('a frase nao é um palindromo!')
