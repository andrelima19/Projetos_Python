#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Andre','Maria', 'Ana', 'Joao')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras.lower(), end='')
