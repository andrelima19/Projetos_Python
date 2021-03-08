# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
data_atual = date.today()
maior_idade = 0
menor_idade = 0

for c in range(1, 7+1):
    ano_nascimento = int(input('Informe sua data de nascimento: '))
    if (data_atual.year - ano_nascimento) >= 18:
        maior_idade += 1
    elif (data_atual.year - ano_nascimento) < 18:
        menor_idade += 1

print(f'Quantidade de pessoas maiores de idade: {maior_idade}\n'
      f'Quantidade de pessoas menores de idade: {menor_idade}')
