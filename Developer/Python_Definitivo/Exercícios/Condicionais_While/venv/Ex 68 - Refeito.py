from random import randint

v = 0
p = 0
while True:
    jogador = int(input('Digite um número: '))
    pc = randint(1,11)
    total = jogador + pc
    tipo= ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR - [P/I]: ')).strip().upper()[0]# Equanto não houver os caracteres especificados, repita
        # o laço.
    print(f'Você jogou {jogador} e computador:{pc}\n'
          f'Total: {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            v +=1
        else:
            print('Você perdeu')
            break
    if total == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v +=1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente.')
print(f'GAME OVER. Você venceu {v} vezes')