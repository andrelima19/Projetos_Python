#Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

# Melhorado por mim
while True:
    resp = ' '
    c = 0
    n = int(input('Digite um número: '))
    if n < 0:
        print('Número Negativo\n'
              'FIM')
        break
    else:
        while c < 10:
            c = c + 1
            print(f'{n} X {c} = {n * c}')
        resp = str(input('Deseja continuar? [S / N]: ')).strip().upper()[0]
        if 'S' in resp:
            while c < 10:
                c = c + 1
                print(f'{n} X {c} = {n * c}')
        else:
            print('FIM')
            break
