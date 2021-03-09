# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

user = 0
tentativas = 0
par = user % 2 == 0
impar = user % 2 == 1

user = int(input('Adivinhe o número que estou pensando: '))
pc = randint(0, 5)

while user != pc:
    print(f'Você errou...Eu pensei no número: {pc}')
    user = int(input('Tente outra vez: '))
    tentativas = tentativas + 1


print(f'Você acertou! Número de tentativas: {tentativas}')
print(f'Você digitou: {user} o PC: {pc}')
