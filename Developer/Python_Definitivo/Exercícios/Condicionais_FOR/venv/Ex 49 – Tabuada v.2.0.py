# Exercício Python 49: Refaça o DESAFIO 9, mostrando a
# tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número: '))

for c in range(1, 11):  # A variável 'C' recebe os valores em sequencia de range.
    print(f'{n} x {c} = {n * c}')
