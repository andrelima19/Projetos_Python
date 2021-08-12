'''
Interactive Help
Docstrings
Argumentos opcionais
Escopo de variáveis
Retorno de resultados
'''

# Interactive Help - É um manual completo dos comandos do python
help(print)
help(input)
# Outra forma -
print(input.__doc__)

#Docstring - Documentação criada por nós mesmos.
def contador(i,f,p):

    '''
    Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: intervalo da contagem
    :return: sem retorno
    '''

    c=i
    while c <= f:
        print(f'{c}', end=' ')
        c+=p
    print('FIM')

contador(1, 10, 2)

help(contador)

# Parametros opcionais - Como escolher não por nenhum valor num parâmetro?
'''
# Função normal
def somar(a,b,c):
    s = a + b + c
    print(f'A soma vale: {s}')
'''
# Função modificada
def somar(a,b,c = 0):
    s = a + b + c
    print(f'A soma vale: {s}')

somar(3,2)

print()
# Escopo de variáveis
# Escopo - Local onde uma variável vai existir.

def funcao():
    n1 = 2
    print(f'N1 dentro vale: {n1}')

n1 = 5

# A mesma variável foi declarada duas vezes: Uma vez dentro do escopo LOCAL (N1 = 2)
# outra vez dentro do escopo GLOBAL (N1 = 5)

funcao()
print(f'N1 fora vale: {n1}')

print()

def funcao2():
    global a
    print(f'N1 dentro vale: {a}')

a = 5

# Quando damos o comando "global" mesmo que a variável esteja dentro do escopo local ela será referenciada como global

print()

funcao2()
print(f'N1 fora vale: {a}')

# Return - Não imprime os valores mas faz o retorno deles (?)

def somar2(a = 0, b = 0, c = 0):
    s = a + b + c
    return s

r1 = somar2(1,3,5)
r2 = somar2(2,4)
r3 = somar2(7)

print(f'Os resultados foram: {r1}, {r2}, {r3}')