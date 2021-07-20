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
Podemos facilmente ORDENAR uma lista EM ORDEM DESCRESCENTE.
'''
lista1.sort(reverse=True)
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
#print(lista2[::-1]) # Slice - Mesmo resultado do reverse
# string[inicio:fim:passo]

'''
Copiar uma lista
'''
lista6 = lista2.copy()
print(lista6)
'''
# Contando elementos de uma lista
'''
print(len(lista1))

'''
Removendo o último elemento de uma lista - POP
Obs: O Pop não apenas remove o último elemento, mas também o retorna.
'''
print(lista5)
lista5.pop()
print(lista5)

'''
Podemos remover um elemento pelo índice - POP(indice)
Obs: Os elementos a direita deste índice serão deslocados para a equerda.
Obs2: Se não houver elemento no índice informado, teremos o erro: 'IndexError'
'''

lista5.pop(2)
print(lista5)

'''
Podemos remover todos os elementos - CLEAR
'''
print(lista5)
lista5.clear()
print(lista5)


''' Podemos repetir os elementos em uma lista. '''
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

''' Convertendo uma lista numa string '''
lista6 = ['Programação', 'em', 'Python:','Essencial']
print(lista6)

'''Abaixo estamos falando: Pega a lista6, coloca o espaço em cada elemento e transforma numa string'''
curso = ''.join(lista6)
print(curso)

'''Utilizando variáveis em listas'''

numeros = [1,2,3,4,5]
print(numeros)

n1 = 1
n2 = 2
n3 = 3

numeros = [n1, n2, n3]
print(numeros)

'''Acesso aos elementos de forma indexada'''

cores = ['verde', 'azul', 'amarelo', 'Vermelho']
print(cores[0])
print(cores[1])
print(cores[2])

'''Fazer acesso aos elementos de forma indexada inversa.'''
'''Para entender melhor o índice negativo, pense na lista como
um circulo onde o final de um elemento está ligado ao inicio da lista'''

print(cores[-1])
print(cores[-2])
print(cores[-3])

'''>>>>>>>>>>>>ENUMARATE<<<<<<<<<<<<'''

lista8 = [9,3,2,1,4]

for c, v in enumerate(lista8):
    print(f'Na posição {c} encontrei o valor: {v}')

'''Colocando valores na lista através do input'''

valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, i in enumerate(valores):
    print(f'Na posição: {c} encontrei o valor: {i}')

'''Listas vinculadas e desvinculadas'''
'''Listas Viculadas'''
a = [1,2,3,4]
b = a # A lista A estará vinculada a Lista B que foi criada. Veja o exemplo

print(f'Lista A: {a}')
print(f'Lista B : {b}')
b[2] = 5
print(f'Lista A: {a}')
print(f'Lista B : {b}')

print('+=' * 20)
print('+=' * 20)

'''Lista desvinculada ou seja apenas uma cópia da outra lista'''
c = [1, 2, 3, 4]
d = c[:]  # A lista D terá apenas uma cópia dos valores em C

print(f'Lista C: {c}')
print(f'Lista D : {d}')
d[2] = 8
print(f'Lista C: {c}')
print(f'Lista D : {d}')

