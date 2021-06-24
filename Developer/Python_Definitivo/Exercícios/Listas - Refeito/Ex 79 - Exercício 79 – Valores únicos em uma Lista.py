# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
resposta = ''

while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor adicionado, não vou adicionar')

    resposta = str(input('Deseja continuar? ')).strip().lower()
    if 'sim' not in resposta:
        break

valores.sort()
print(f'Fim do programa. Sua lista contém os seguintes números: {valores}')
