# TUPLAS - TEORIA
'''
Uma variável só pode armazenar um valor. Ela ocupa apenas UM espaço na memória. Mas e se você quiser armazenar
mais de um valor na variável?
Nesse caso faremos uso de variáveis compostas.

variaves simples
Ex: x = 1
Só armazenam um valor

Variáveis compostas podem armazenar mais de um valor.
As variáveis compostas podem ser:
Tuplas; ()
Listas; []
Dicionários {}
() - Tupla
[] - Lista
{} - Dicionário


Os elementos de uma tuplo são acessados através dos índices.

As Strings são variáveis compostas

Podemos fazer o fatiamento de tuplas e usar o For

Considere a variavel composta 'lanche'

lanche = 'hamburger', 'suco', 'pizza', 'pudim'
print(lanche[2]) - imprime pizza
print(lanche[0:2]) - imprime hamburger e suco
print(lanche[1:]) - imprime de suco até o final que é pudim
print(lanche[-1]) - Imprime o ultimo elemento que é o pudim (Imprime reverso)
print(len(lanche)) - Imprime o comprimento da variavel lanche, no caso: 4

Uso do FOR

for c in lanche:
    print(c)

AS TUPLAS SÃO IMUTÁVEIS

'''

# PRÁTICA #
# Diferenciação importante
'''
() - Tupla
[] - Lista
{} - Dicionário

Obs: Não há mais necessidade de colocar parenteses
'''
lanche  = ('hamburger', 'suco', 'pizza', 'pudim')
print(lanche)
print(type(lanche))

print(lanche[1]) # Imprime o indice 1
print(lanche[-2]) # Imprime ao inverso
print(lanche[1:3]) # Comecça do indice 1 e vai até o 3 (Desconsidera o indice 3)
print(lanche[1:]) # De um ponto até o final
print(lanche[:3]) # Do inicio até um ponto
print(lanche[-2:]) # Começa na pizza e vai até pudim

# Tuplas são imutáveis
'''
lanche[1] = 'Refrigerante'
print(lanche) # Da erro

                'tuple' object does not support item assignment
Os objetos do tipo tupla não podem ter valores atribuídos, ou seja, não podemos atribuir valores as tuplas
a não ser que seja na declaração delas.
'''

# FOR
'''
lanche2 = ('Batata', 'feijão', 'Arroz', 'bife', 'Farofa')
for comida in lanche2:
    print(f'Comi: {comida}')

print('Comi MUUUITO')

lanche3 = ('Batata', 'feijão', 'Arroz', 'bife', 'Farofa')
for cont in range (len(lanche3)):
    print(f'Eu vou comer {lanche[cont]} na posição: {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição: {pos}')
'''

print(sorted(lanche)) # Colocando em ordem
print(lanche)

a = (2, 4, 6, 8)
b = (1,3,5,7,9)
c = a + b
print(c)
print(c.count(2)) # Contando elementos

# index - Em que posição está o elemento
print(c.index(3))

# As tuplas aceitam dados de tipos diferentes dentro delas

cadastro = ('André', 31, 'Rio de Janeiro')
print(cadastro)

# Delete na tupla
# Embora a tupla seja imutável ela aceita ser apagada, mas somente toda ele e não algum elemento especifico

cadastro1 = ('Kaillen', 31, 'Rio de Janeiro')
print(cadastro1)

del cadastro1
print(cadastro1)





