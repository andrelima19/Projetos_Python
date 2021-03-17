# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.
'''
# Primeira vez que fiz

res = ''

print('Bem-vindo ao jogo do PAR OU IMPAR!\n')
print('PAR\n'
      'IMPAR\n')

escolha = str(input('Escolha uma das opções acima: ')).strip().lower()
n = int(input('Agora digite um número: '))

while 'VOCÊ VENCEU!' in res:
    if 'par' in escolha:
        if n % 2 == 0:
            res = 'VOCÊ VENCEU!'
            #print('PAR')
        if n % 2 == 1:
            print('PERDEU!')

    if 'impar' in escolha:
        if n % 2 == 1:
            res = 'VOCÊ VENCEU!'
            #print('IMPAR')
        if n % 2 == 0:
            print('ERRO!')
'''

from random import randint

while True:
    user = int(input('Digite um número: '))
    pc = randint(1, 21)
    total = user + pc
    opcao = ' '
    total = v = 0

    while opcao not in 'PI':
        opcao = str(input('Escolha entre PAR ou IMPAR [P / I]: ')).strip().upper()[0]
    print(f'Você digitou {user} o computador: {pc} - Total: {total}')

    if opcao == 'P':
        if total % 2 == 0:
            v +=1
            print('VOCÊ VENCEU! Você escolheu PAR e o total foi: ', total)
        else:
            print('Você perdeu :D')
            break
    if opcao == 'I':
        if total % 2 == 1:
            v +=1
            print('VOCÊ VENCEU! Você escolheu IMPAR e o total foi: ', total)
        else:
            print('Você perdeu :(')
            break

print(f'GAME OVER. Você venceu {v} vezes')

