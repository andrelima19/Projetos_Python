# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).


n = 0
c = 0
soma = 0
print('Digite qualquer número. \n'
      'Pare a qualquer momento digitando 999.\n'
      '\n')

while n != 999:
    n = int((input('Digite um número: ')))
    soma += n
    c += 1

print(f'Soma dos valores digitados: {c - 1, soma - 999}\n'
      f'Quantidade de valores digitados: {c}')