#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

'''
lista_princ = []

num_lin = int(input('Quantas linhas você deseja? '))
num_col = int(input('Quantas colunas você deseja? '))


for lin in range(num_lin):
    lista_princ.append(list())
for col in range(num_col):
    lista_princ.append(list())

for lin in range(num_lin):
    for col in range(num_col):
        lista_princ[lin].append((int(input(f'Valores para: [{lin}][{col}]: '))))
print(lista_princ)
'''

lista_princ = []
linhas = list()

num_linha = int(input('Digite o número de tentativas: '))

for tentativas in range(num_linha):
    for sorteio in range(1,7):
       lista_princ.append(sorteio)
    print(lista_princ)