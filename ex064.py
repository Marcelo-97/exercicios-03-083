num = cont = soma = 0 # todos sao 0
num = int(input('Digite um número [999 para parar]: ')) # primeiro numero do usuario
while num != 999:    # enquanto o numero digitado for diferente de 999 o while nao para
    soma += num   # soma = soma + num  # 'soma' é somado com 'num' (ex: se 'num==2' ele sera somado com 0 pois num==2, ou seja 0+2=2, portanto 'soma'==2 agora
    cont += 1 # cont = cont +1  #  são contados numeros foram digitados
    num = int(input('Digite um número [999 para parar]: '))   # pergunta novamente algum numero para o usuario, caso seja '999' saira do while

print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont,soma)) #fim do programa
