#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

cadastro = list()
pessoa = dict()

resp = ''
total_idade = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa.copy())

    total_idade = pessoa['idade'] + total_idade
    media_idade = (total_idade / len(cadastro))

    resp = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if 'S' not in resp:
        break

print(f'Número de pessoas cadastradas: {len(cadastro)}')

print('>>> Pessoas cadastradas <<<<')
for p in cadastro:
    print(f'Nome: {p["nome"]}\n'
          f'Sexo: {p["sexo"]}\n'
          f'Idade: {p["idade"]}')
    print('+=' * 5)


print(f'Média de idade: {media_idade}')

print('>>> Lista de mulheres cadastradas <<<')
for p in cadastro:
    if p["sexo"] in 'F':
        print(f'Nome: {p["nome"]}')

print('>>> Pessoas com idade acima da média <<<')
for p in cadastro:
    if p['idade'] > media_idade:
        print(f'Nome: {p["nome"]} está com idade acima da média')
