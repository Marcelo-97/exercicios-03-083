n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}'.format(n1, n2, media))
    print('O aluno está REPROVADO')
elif media >=5.0 and media <6.9:
    print('Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}'.format(n1, n2, media))
    print('O aluno está de RECUPERAÇÃO')
elif media > 7.0:
    print('Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}'.format(n1, n2, media))
    print('O aluno está APROVADO')