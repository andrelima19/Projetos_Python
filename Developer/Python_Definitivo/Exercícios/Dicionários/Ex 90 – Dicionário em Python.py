#Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

# COMO EU RESOLVI
aluno = list()
situacao = dict()

aluno.append(str(input('Nome do aluno: ')))
aluno.append(float(input('Média do aluno: ')))

if aluno[1] <=4:
    situacao['situacao1'] = 'Reprovado'
    print(f'Aluno: {aluno[0]}\n'
          f'Média: {aluno[1]}\n'
          f'Situação:{situacao["situacao1"]}')

elif aluno[1]>4 and aluno[1] <= 6:
    situacao['situacao2'] = 'Em recuperação'
    print(f'Aluno: {aluno[0]}\n'
          f'Média: {aluno[1]}\n'
          f'Situação: {situacao["situacao2"]}')

elif aluno[1]>6 and aluno[1]<=10:
    situacao['situacao3'] = 'Aprovado'
    print(f'Aluno: {aluno[0]}\n'
          f'Média: {aluno[1]}\n'
          f'Situação: {situacao["situacao3"]}')

# PROFESSOR
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] <4:
    aluno['situacao'] = 'Reprovado'
elif aluno['media']>=4 and aluno['media'] <=7:
    aluno['situacao'] = 'Em Recuperação'
else:
    aluno['situacao'] = 'Aprovado'

print(aluno.items())
for k, v in aluno.items():
    print(f'{k} é igual a {v}')