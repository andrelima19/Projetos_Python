# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva(‘Olá, Mundo!’)
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(msg):
    num = '~'
    tam = len(msg)
    print(num * tam)
    print(msg)
    print(num * tam)

escreva('Curso de Python')
escreva('Curso de Python - Curso em Vídeo')
escreva('Curso de Python - Curso em Vídeo - Gustavo Guanabara ')