
'''
LISTAS

Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
'''
# Adicionando elementos na lista
# append (Adiciona elementos no final da lista
#Ex:
listadecompra = []
listadecompra.append('arroz')

#Insert - Adiciona elementos em outras posições da lista
#Ex:
listadecompra.insert(1,'arroz') #O elemento arroz foi adicionado na posição 1

# Apagando elementos
# Del
#Ex:
del listadecompra[1]

#pop - Normalmente usado para apagar o último elemento mas pode ser usado para apagar em qualquer posição
#Ex
listadecompra.pop()
listadecompra.pop(3)

#remove - Remove ou apaga pelo conteúdo, não pela posição
#Ex:
listadecompra.remove('arroz')

'''
Criando uma lista com o range
'''
valores = list(4,11)

# Ordeando uma lista
# sort
valores = [1,3,9,4,6,0,23,12,5]
valores.sort()

# Ordenando de forma reversa
valores.sort(reverse=True)

#Tamanho da Lista
#len

len(valores)