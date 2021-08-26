'''
Exercício Python 108: Adapte o código do desafio #107,
criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
'''

import moeda

n = float(input('Digite o preço: '))
print(f'O valor: {moeda.moeda(n)} acrescido de 10% é: {moeda.aumentar(n)}\n'
      f'O valor: {moeda.moeda(n)} reduzido de 15% é: {moeda.diminuir(n)}\n'
      f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}\n'
      f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')