expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr: #para cada simbolo "simb"
    if simb == '(':  # se houver um "(" parenteses aberto
        pilha.append('(') # sera adicionado a lista "pilha"
    elif simb == ')': # se houver um parenteses fechado
        if len(pilha) > 0:  # se o total de elementos dda lista "len(pilhas) for maior que 0
            pilha.pop() # ".pop()" retira o ultimo elemento da lista
        else:
            pilha.append(')')  # aqui teve mais parenteses fechando do que abrindo
            break
if len(pilha) == 0:  #se o total de elementos da pilha for igual a 0
    print('sua expressão esta valida.')
else:
    print('sua expressão não esta valida.')
