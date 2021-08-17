
'''
#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e  vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

# numeros = []
# def sorteio() - Sortear 5 números e colocar dentro da lista
# def somaPar() - Somar valores pares

'''
'''
# Criar lista - numeros
# funçao sorteia
    # sortear 5 numeros
    # Colocar os 5 numeoros na lista
     
# função somaPar
    # somar os numeros pares da lista anterior
'''
numeros = []
soma_Pares = []

def sorteia():
    from random import randint
    for c in range(1, 6):
        n = randint(1, 15)
        numeros.append(n) # numeros sorteados de 1 a 15
        if n % 2 == 0:
            soma_Pares.append(n)
    print(f'Números sorteados: {sorted(numeros)}')
    print(f'Números pares sorteados: {sorted(soma_Pares)}')
    print()
def somaPar():
    soma = 0
    for c in soma_Pares:
        soma = soma + c
    print(f'Valores pares: {sorted(soma_Pares)}\n'
          f'Soma dos pares: {soma}')

sorteia()
somaPar()