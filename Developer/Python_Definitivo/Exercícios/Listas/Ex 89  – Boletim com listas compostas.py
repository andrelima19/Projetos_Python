# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
ficha = []

while True:
    nome = str(input('Informe o nome do aluno: '))
    nota1 = float(input('Informe a 1º nota: '))
    nota2 = float(input('Informe a 2º nota: '))
    media = ((nota1 + nota2)/2)
    ficha.append([nome, [nota1, nota2], media])

    resp = str(input('Deseja continuar [S/N]? ')).strip().lower()
    if resp in 'Nn':
        break

boletim.append(ficha)

print('+=' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<4}{a[2]:>12.1f}')

while True:
    opcao = int(input('Mostrar as notas de qual aluno?(999 interrompe)'))
    if opcao == 999:
        print('Finalizando ...')
        break
    if opcao <= len(ficha) -1:
        print(f'Notas de {ficha[opcao][0]} são: {ficha[opcao][1]}' )