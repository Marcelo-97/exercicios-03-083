palavras=('aprender','programar ','linguagem',' python ','curso ','gratis',' estudar',' praticar ','trabalhar ','mercado ','programador',' futuro')
for p in palavras: # uma laço para as "palavras"
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:# para cada "letra" em "p"
        if letra.lower() in 'aeiou':# se tiver "aeiou"
            print(letra,end='')#a vogal ira ser printada


