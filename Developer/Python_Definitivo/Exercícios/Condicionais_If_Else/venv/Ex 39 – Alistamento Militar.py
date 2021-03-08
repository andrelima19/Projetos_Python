#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('Informe a sua idade para verificar se pode se alistar: '))

if idade == 18:
    print(f'Você já está na idade de alistar.')
elif idade > 18:
    print('Você já passou da idade para se alistar.')
else:
    print(f'Você ainda não pode se alistar. Faltam {(18 - idade)} anos para poder se alistar.')