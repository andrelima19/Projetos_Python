#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

valores = []
numero  = 0
cont = 0
resposta = ''

for posicao in range(0,5):
    numero = int(input('Digite um valor inteiro: '))
    #cont = cont + 1
    if valores == []:
        valores.insert(0,numero)
    else:
        if numero > valores[0]:
            valores.insert(1,numero)
        if numero < valores[0]:
            valores.insert(0, numero)


print(valores)
