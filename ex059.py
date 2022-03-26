import time

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o seundo valor '))
opção = 0

while opção !=5:
        print('''            [1] somar
            [2]multiplicar
            [3]maior
            [4]novos numeros
            [5]sair do prorama ''')
        opção = int(input('Qual a sua opção? '))
        if opção == 1:
            resultado = n1 + n2
            print('A soma entre {} e {} é igual a {}'.format(n1, n2, resultado))
        elif opção == 2:
            resultado = n1 * n2
            print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, resultado))
        elif opção == 3:
            if n1 > n2:
                print('O numero {} é maior que o numero {} '.format(n1, n2))
            elif n1 < n2:
                print('O numero {} é menor que o numero {}'.format(n1, n2))
            elif n1 == n2:
                print('O numero {} é o numero {} são iguais'.format(n1, n2))
        elif opção == 4:
            print('Informe os numeros novamente')
            n1 = int(input('Digite o primeiro valor: '))
            n2 = int(input('Digite o segundo valor: '))
        elif opção >5:
            print('Opção inválida. Tente novamente.')
        elif opção == 5:
                print('Finalizando...')
        print('=-=' * 10)
        time.sleep(1)
print('Fim do programa! Volte sempre!')
