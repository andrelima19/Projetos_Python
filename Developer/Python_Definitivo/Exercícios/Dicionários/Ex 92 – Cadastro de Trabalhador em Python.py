# Exercício Python 092: Crie um programa que leia nome,
# ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

#nome, ano de nascimento, número ctps, ano de contratação, salário
# Tempo para se aposentar

carteira = dict()

carteira['nome'] = str(input('Informe seu nome: '))
carteira['ano de nascimento'] = int(input('Informe o ano em que nasceu: '))
carteira['ctps'] = int(input('Número da carteira de trabalho (0 sai): '))
carteira['ano de contratação'] = int(input('Ano de contratação: '))
carteira['salario'] = float(input('Informe seu salário: '))

carteira['tempo para aposentadoria'] = ( 2021 - carteira['ano de nascimento']) - ( 2021 - carteira['ano de contratação'])

print(f'Nome: {carteira["nome"]}\n'
      f'Ano de Nascimento: {carteira["ano de nascimento"]}\n'
      f'CTPS: {carteira["ctps"]}\n'
      f'Ano de contratação: {carteira["ano de contratação"]}\n'
      f'Salário: { carteira ["salario"]}\n'
      f'Tempo para se aposentar: {carteira["tempo para aposentadoria"]} anos')