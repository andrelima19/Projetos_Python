''''''
'''
Exercício Python 109: Modifique as funções que form criadas no desafio 107 
para que elas aceitem um parâmetro a mais, informando se o valor retornado 
por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''

import moeda

n = float(input('Digite o preço: '))
print(f'O valor: {moeda.moeda(n)} acrescido de 10% é: {moeda.aumentar(n, 10, True)}\n'
      f'O valor: {moeda.moeda(n)} reduzido de 15% é: {moeda.diminuir(n, 15, True)}\n'
      f'O dobro de {moeda.moeda(n)} é {(moeda.dobro(n, True))}\n'
      f'A metade de {moeda.moeda(n)} é {(moeda.metade(n, True))}')

'''Usando o Help para exibir as informações da função criada'''
print(help(moeda))
print(moeda.__doc__)