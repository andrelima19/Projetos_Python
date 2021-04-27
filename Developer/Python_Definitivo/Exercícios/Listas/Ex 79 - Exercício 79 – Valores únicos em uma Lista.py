# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
resposta = ''

while resposta in 'sim' :
    valores.append(int(input('Digite um número: ')))
    resposta = input(str('Deseja continuar: ')).strip().lower()
    if 'nao' in resposta:
        break



print(valores,'FIM')