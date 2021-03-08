# Exercício Python 24: Crie um programa que leia o nome de uma
# cidade e diga se ela começa ou não com o nome “SANTO”.

nome = str(input('Digite o nome de uma cidade: '))
separa = nome.upper().split()
cidade = "SANTO" in separa[0]
print(separa)

if cidade == True:
    print('A cidade começa com o nome "Santo".')
else:
    print('A cidade não começa com o nome "Santo".')


