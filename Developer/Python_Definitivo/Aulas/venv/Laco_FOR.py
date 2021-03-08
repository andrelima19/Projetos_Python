# FUNÇÃO RANGE É COMPOSTA DE 3 PARÂMETROS.
# start, stop, step
# Ex: for c in range (0, 5, 2) - 0 (Começa do zero); 5 - (Para no 5); 2 - (Pula de dois em dois)
# Não necessariamente os 3 devem ser utilizados.

'''
for x in range (0,6):
    print('Oi!')
print('FIM')

print('======')
'''
for c in range (0,6): # Para C no intervalo entre 0 e 6, imprima C. (C vai receber os valores de 0 a 6)
    print(c * 2)
print('FIM')

'''
print('======')

for c in range (0, 7, 2): # Começa do 0; Vai ateo 7 e puld de 2 em 2.
    print(c)
print('FIM')

print('======')


n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
'''

print('======')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo/Pulo: '))

for x in range(i, f, p):
    print(x)