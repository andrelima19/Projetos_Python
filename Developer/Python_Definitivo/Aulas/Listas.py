# LISTAS EM PYTHON
'''

Listas em pyhton funcionam como vetores ou matrizes ou Arrays em outras linguagens, com a diferença de serem DINÂMICAS
e podermos colocar QUALQUER tipo de dado.

Linguagens C / Java: Arrays
    - Possuem tamnho e tipo de dado fixo:
    Nestas linguagens se você criar um array do tipo int e com tamnho 5,
    este array será sempre do tipo inteiro e ter[a no máximo
    5 valores;

Dinâmico: Não possui tamanho fixo. Você não define tamanho, podemos criar a lista
e simplesmente ir adicionando elementos.
Essa lista não é infinita, ela depende da quantidade de memória disponível.

Qualquer tipo de dado: As listas não possuem tipo de dado fixo.

As listas em python são representadas por colchetes: []
'''


lista1 = [1, 89, 3, 4, 6, 5, 5, 7, 255]
lista2 = ['R', 'E', 'D', 'E', '', 'S', 'O', 'C', 'I', 'A', 'L']
lista3 = []
lista4 = list(range(11))
lista5 = list('Meu nome:')

print(lista5)

'''
Podemos facilmente checar se determinado valor está contido na lista.
'''
num = 8
if num in lista4:
    print('Encontrei o numero: ', num)
else:
    print('Não encontrei')

'''
Podemos facilmente ORDENAR uma lista.
'''
lista1.sort()
print(lista1)

'''
Podemos facilmente contar o número de ocorrências de um valor em uma lista.
'''
print(lista1.count(5))
print(lista5.count('e'))

'''
Para adicionar elementos numa lista usamos a função: APPEND
Obs. Com o append só conseguimos adicionar um elemento por vez e sempre no final da lista.
'''
print(lista1)
lista1.append(49)
print(lista1)

'''
Podemos adicionar uma lista dentro de outra lista
'''

lista1.append([0, 34, 1, 11, 13]) # Coloca a lista como elemento único (sublista)
print(lista1)

if [0, 34, 1, 11, 13] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei.')

'''
Para adicionar VÁRIOS ELEMENTOS numa lista usamos a função: EXTEND
Ele não aceita valor único, apenas iteráveis.
Assim como o append os elementos são adicionados ao final da lista.
'''
print(lista1)
lista1.extend([4, 22, 34,56, 89,10])
print(lista1)

'''
Podemos inserir um novo valor a lista informando a posição do Índice.
'''
print(lista1)
lista1.insert(0, 'novo valor')
print(lista1)

'''
Podemos juntar duas listas
'''
lista1 = lista1 + lista2
# Ou lista1 = lista1.extend(lista2)
print(lista1)

'''
Podemos inverter uma lista com a função: reverse
'''
# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista2)
print(lista2[::-1]) # Slice - Mesmo resultado do reverse
# string[inicio:fim:passo]