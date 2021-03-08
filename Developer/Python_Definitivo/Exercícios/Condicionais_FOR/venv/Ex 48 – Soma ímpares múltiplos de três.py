# Exercício Python 48: Faça um programa que calcule a soma entre todos
# os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
c = 0
for multip3 in range(1,501,2): # Números ímpares.
    if multip3 % 3 == 0:
        print(multip3, end='-')
        c = c + 1
        soma = soma + multip3
print('\n')
print(f'Quantidade dos múltiplos de 3: {c}')
print(f'Soma dos múltiplos de 3: {soma}')



'''
    soma = soma + multip3
    c = c + 1
print(f'Quantidade dos múltiplos de 3: {c}')
print(f'Soma dos múltiplos de 3: {soma}')
'''