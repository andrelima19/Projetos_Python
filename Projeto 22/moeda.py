
'''
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

def aumentar(valor):
    aumento = (valor*0.1) + valor
    return aumento

def diminuir(valor):
    reduzir = valor - (valor*0.15)
    return reduzir

def dobro(valor):
    dobrar = (valor*2)
    return dobrar

def metade(valor):
    meio = (valor/2)
    return meio

def moeda(valor):
    formatacao = f'R$ {valor:.2f}'
    return formatacao

x = int(input('Valor: R$'))
print(f'{moeda(x)}')