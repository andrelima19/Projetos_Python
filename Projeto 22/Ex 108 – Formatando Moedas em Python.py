'''
Exercício Python 108: Adapte o código do desafio #107,
criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
'''

import moeda

n = float(input('Digite o preço: R$ '))
print(f'O valor: {n} acrescido de 10% é: {moeda.aumentar(n)}\n'
      f'O valor: {n} reduzido de 15% é: {moeda.diminuir(n)}\n'
      f'O dobro de {n} é: {moeda.dobro(moeda.moeda(n))}\n'
      f'A metade de {n} é {moeda.metade(n)}')