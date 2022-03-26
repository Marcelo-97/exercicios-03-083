valores = list()
men = 0
mai = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um Valor na posição {v}: '))) #o usuario digita os numeros na lista
    if v == 0:
        mai = men = valores[v] #verifico se existe apenas um valor digitado
    else:
        if valores[v] > mai: #verifico qual o maior valor
            mai = valores[v]
        if valores[v] < men:#verifico qual o menor valor
            men = valores[v]
print(f'Voce digitou os valores{valores}\n')
print(f'O maior valor digitado foi {max(valores)} nas posições', end='')
for i, c in enumerate(valores): # procuro atraves do indice "i" aonde esta o maior valor
    if c == mai:
        print(f' {i}...', end='')
print(f'\nO maior valor digitado foi {min(valores)} nas posições', end='')
for i, c in enumerate(valores):# procuro atraves do indice "i" aonde esta o menor valor
    if c == men:
        print(f' {i}...', end='')
