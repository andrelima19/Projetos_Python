'''
Interactive Help
Docstrings
Argumentos opcionais
Escopo de variáveis
Retorno de resultados
'''

'''DOCUMENTAÇÃO'''
'''Help e __doc__'''

'''Interactive Help - É um manual completo dos comandos do python
O interactive help é mais verboso, sendo uma consulta mais detalhada.
'''
help(int)

'''__doc__ faz uma consulta mais simples, exibindo as informações a respeito
dos comandos de forma suscinta.'''

print(int.__doc__) # comando + . + __doc__
print(float.__doc__)

'''DOCSTRINGS --> CRIANDO SUA PRÓPRIA DOCUMENTAÇÃO'''
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

'''# Parametros opcionais - Como escolher não por nenhum valor num parâmetro?'''
# Função normal
def somarA(a,b,c):
    s = a + b + c
    print(f'A soma vale: {s}')
'''
# Função com UM parametro opcional
'''
def somarB(a,b,c = 0):
    s = a + b + c
    print(f'A soma vale: {s}')

somarB(3,2)

'''Função com TODOS os parametros opcionais'''
def somarC(a=0,b=0,c=0):
    s = a + b + c
    print(f'A soma vale: {s}')
somarC()


'''# Escopo de variáveis
   # Escopo - Local onde uma variável vai existir.
'''

def funcao():
    n1 = 2 # Escopo local
    print(f'N1 dentro vale: {n1}')

n1 = 5 # Escopo global

funcao() # Chamando a função
# A mesma variável foi declarada duas vezes:
# Uma vez dentro do escopo LOCAL (N1 = 2)
# outra vez dentro do escopo GLOBAL (N1 = 5)
print(f'N1 fora vale: {n1}')


def funcao2():
    global a
    a = 1
    b = 2
    c = 3
    print(f'A dentro vale {a}\n'
          f'B dentro vale {b}\n'
          f'C dentro vale {c}')
a = 2
b = 5
c = 7

funcao2()
print(f'A fora vale: {a}')

# Quando damos o comando "global"
# mesmo que a variável esteja dentro do escopo local ela será referenciada como global -

'''RETORNANDO VALORES - RETURN'''
'''Modo tradicional com o retorno vindo pelo Print'''
def somar3(a=0,b=0,c=0):
    s = a + b+ c
    print(f'A soma vale: {s}')

somar3(2,4,5)
somar3(1,0,3)
somar3(2)
somar3(1,3,10)
somar3(9,3)
'''Observe que todos os retornos vieram da mesma forma, mesma formatação'''

'''Usando o Return'''
def somar4(a=0,b=0,c=0):
    s = a + b + c
    return s
resp1 = somar4(3,2)
print(f'As somas valem {resp1}')

resp2 = somar4(3)
print(f'A soma vale {resp2}')

'''Observe que agora, com o retorno da função, podemos personalizar a forma de como 
queremos que o resultado seja exibido'''

'''Mais exemplos'''
def exemplo1():
    s = 4
    return s

print(exemplo1())
y = exemplo1()
print(y)
########################
def exemplo2(a,b):
    s = a + b
    return s

print(exemplo2(3,8))

x = exemplo2(2,10)
print(x)