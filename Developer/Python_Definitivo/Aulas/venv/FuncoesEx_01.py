
def soma(a, b):
    s = a + b
    print(s)

soma(3,4)
soma(1,2)
soma(9,0)


'''Chamando a função de forma mais "bonitinha"'''
def outra_soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma é igual: {s}')

print()

outra_soma(a=4, b=1) # Explicitando os parametros
outra_soma(8,2)

'''EMPACOTAMENTO DE PARAMETROS'''

def contador(* num):
    print(num)

contador(0,3,12,2,1,2)
contador(0,3,)
contador(3,1,5)

print()

def contador(* num):
    for valor in num:
        print(f'{valor}', end='')
    print('Fim')

contador(0,3,12,2,1,2)
contador(0,3,)
contador(3,1,5)

print()

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo: {tam} números.')

contador(0,3,12,2,1,2)
contador(0,3,)
contador(3,1,5)