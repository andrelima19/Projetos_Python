# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

'''
resposta = 0
while resposta != 'M' and resposta != 'F':
    resposta = str(input('Digite o sexo do usuário [M / F]: ')).upper()

print('FIM')
'''

sexo = str(input('Informe o seu sexo [S / F]: ')).strip().upper()[0]
while sexo not in 'MmFf': # NOT IN - Se não for encontrado na variável (os valores) ....
    sexo = str(input('Valor inválido. Informe seu sexo [S / F]: ')).strip().upper()[0]
print(f'{sexo} - Sexo digitado corretamente\n'
      f'FIM')