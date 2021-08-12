# Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt():
    n = input('Informe UM valor númerico: ')

    while True:
        if n.isnumeric() and len(n) == 1:
            n = int(n)
            print(f'CORRETO!\n'
                  f'Valor: {n}')
            break

        elif len(n) > 1:
            n = input('ERRO! Insira apenas UM valor: ')
        else:
            n = input('Você inseriu um carcatere. Insira apenas UM valor NÚMERICO: ')

leiaInt()