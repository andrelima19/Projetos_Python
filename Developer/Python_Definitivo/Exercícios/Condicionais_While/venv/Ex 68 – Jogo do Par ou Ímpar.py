# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

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
