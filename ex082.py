valores = []
par = []
impar = []
resp = ' '
while True:
    valores.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(valores):  # aqui vou verificar o valor dentro de cada indice e numerar "enumerate" a lista "valores"
    if v % 2 == 0:               # "i" sendo o indice, valor "v" dentro do indice ("indice" ou "posição" do valor)
        par.append(v)
    if v % 2 == 1:
        impar.append(v)

print(f'Os valores digitados foram {valores}')
print(f'Os valores pares são {par}')
print(f'Os valores impares são {impar}')