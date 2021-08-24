# Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

''''
def leiaInt():
    num = input('Digite UM número: ')
    while True:
        if num.isnumeric() and len(num) == 1:
            return 'correto'

        elif len(num) > 1:
            num = input('Digite apenas UM valor: ')

        elif num == str(num) or len(num) > 1:
            num = input('Você digitou uma string, digite um NÚMERO: ')

print(leiaInt())
'''
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você digitou: {n}')