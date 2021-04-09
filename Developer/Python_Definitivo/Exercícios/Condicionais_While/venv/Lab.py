
# Maior e menor
'''
maior = menor = 0
resp = ''
c = 0
while resp in 'S':
    n1 = int(input('Digite um valor inteiro: '))
    n2 = int(input('Digite outro inteiro: '))
    resp = str(input('Deseja continuar?'))

'''
'''
soma = 0
n = 0
c = 0
while c < 5:
    c = c +1
    n = int(input('Digite um número: '))
    soma = soma + n
    print(soma)



print(f'Maior: {maior} - Menor: {menor}', end=' ')
'''
primeiro = segundo = terceiro = 0
maior = menor = 0
primeiro = int(input('Digite um número: '))
segundo = int(input('Digite outro número: '))

if primeiro > segundo:
    maior = primeiro
    menor = segundo
else:
    maior = segundo
    menor = primeiro

print(f'Maior: {maior} - Menor: {menor}')