'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

'''Minha solução
# criar umma lista que irá receber diversos valores
# verificar qual desses valores é o maior
'''

#Primeira solução

def maior(n):
    varios = []
    for c in range(n):
        varios.append(input('Digite um número: '))
    print(f'Números digitados: {sorted(varios)}\n'
          f'O maior número foi: {max(varios)}')

num = int(input('Números a serem digitados: '))
maior(num)


#Segunda solução

def maior():
    mai = men = 0
    c = 0

    while True:
        n = int(input('Número inteiro: '))
        c += 1
        if c == 1:
            mai = men = n
        else:
            if n > mai:
                mai = n
            if n < mai:
                men = n

        resp = str(input('Deseja continuar? ')).strip().upper()
        if 'S' not in resp:
            break

    print(f'Maior: {mai} - Menor: {men}')

maior()
