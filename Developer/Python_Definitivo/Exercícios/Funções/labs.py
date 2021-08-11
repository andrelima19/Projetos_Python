# FUNÇÕES SEM PARÂMETROS
def linhas():
    print('-=' * 30)



linhas()
linhas()
linhas()

def soma():
    print(100)

soma()

# FUNÇÕES COM PARÂMETROS

def mensagem(txt): # Função recebe um parâmetro
    print('*=' * 30)
    print(txt)
    print('*=' * 30)

print()

mensagem('CURSO EM VÍDEO')
mensagem('Teste def')
mensagem('Teste def 2')

print()

def soma2(a,b):
    s = a + b
    print(s)

soma2(3,11)

x = 1

print(type(x))