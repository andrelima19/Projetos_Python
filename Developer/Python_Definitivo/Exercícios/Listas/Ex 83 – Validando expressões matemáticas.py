# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = 0
lista = []

expressao = str(input('Digite uma expressao númerica: '))
lista.append(expressao)

if '(' not in expressao[0]:
    print('ERRO')
elif ')' not in expressao[:]:
    print('ERRO')
else:
    print('Deu certo')