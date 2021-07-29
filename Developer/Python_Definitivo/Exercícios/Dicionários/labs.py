'''
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
'''

cadastro = list()
jogador = dict()

total_gols = 0

while True:
    jogador['nome'] = str(input('Nome: ')).capitalize()
    jogador['partidas'] = int(input('Partidas: '))

    for j in range(jogador['partidas']):
        print(j)