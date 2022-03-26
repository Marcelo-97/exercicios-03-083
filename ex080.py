valores=[]
for c in range(0,5):
    n=int(input('Digite um valor: '))
    if c==0 or n > valores[-1]: # se o numero for o primeiro ou maior do que o ultimo
        valores.append(n)
        print('O numero foi adicionado no final da lista')
    else:
        pos = 0
        while pos < len(valores): # vai verificar da posição 0 até a ultima posição
            if n <= valores[pos]: # verificar dentro de cada posição da lista se o "n" é menor ou igual ao numero naquela posição
                valores.insert(pos,n) # "insert" joga o numero daquela posição para frente e insere esse numero no lugar
                print(f'foi adicionado na posição {pos}')
                break
            pos+=1 # para ir passando para a proima posição
print(f'Os valores digitados foram {valores}')

