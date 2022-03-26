total18 = totalh = totalm20 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))  # criaçao da variavel "idade"
    sexo = ' '  # criação da variavel "sexo"
    while sexo not in 'MF':  # enquanto variavel "sexo" nao tiver M ou F o programa nao ira proseguir
        sexo = str(input('Sexo: ')).strip().upper()[0]  # input de "M" ou "F"
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalh += 1
    if sexo == 'F' and idade < 20:
        totalm20 += 1
    resp = ' '  # criaçao da variavel "resp"
    while resp not in 'SN':  # enquanto a variavel "resp" nao tiver S ou N o programa nao ira continuar
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]  # input de S ou N
    if resp == 'N':  # se o usuario digitar N o break ira acontecer
        break
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todo temos {totalh} homens cadastrados')
print(f'E temos {totalm20} mulheres com menos de 20 anos')
