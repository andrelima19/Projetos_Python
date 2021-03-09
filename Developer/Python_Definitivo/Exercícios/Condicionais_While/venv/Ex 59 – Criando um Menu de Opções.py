# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

somar = multiplicar = maior = novo_numero = sair = 0
opcao = 0
resp = 0


print('Menu:\n'
      '[ 1 ] Somar\n'
      '[ 2 ] multiplicar\n'
      '[ 3 ] maior\n'
      '[ 4 ] novos números\n'
      '[ 5 ] sair do programa')

while opcao != 5:
    n1 = float(input('Insira um valor: '))
    n2 = float(input('Insira outro valor: '))
    opcao = int(input('Insira uma das opções listadas a cima: '))

    if opcao == 1:
        somar = (n1 + n2)
        print(f'Soma dos valores {n1} e {n2}: {somar}')

    elif opcao == 2:
        multiplicar = (n1 * n2)
        print(f'Produto dos valores {n1} e {n2}: {multiplicar}')
        opcao = int(input('Deseja continuar? '))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        if n2 > n1:
            maior = n2
        print(f'O maior valor entre {n1} e {n2} é: {maior}')
        opcao = int(input('Deseja continuar? '))

    elif opcao == 4:
        n1 = float(input('Insira um valor: '))
        n2 = float(input('Insira outro valor: '))
        opcao = int(input('Insira uma das opções listadas a cima: '))


