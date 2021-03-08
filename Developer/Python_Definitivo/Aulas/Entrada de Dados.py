"""
Recebendo dados
Print

Em Pyhon, String é tudo que estiver entre:
- Aspas simples;
- Aspas Duplas;
- Aspas simples triplas; '''
- Aspas duplas triplas; """


print('Informe seu nome: ')
nome = input() # Input -> Entrada de dados

# Print antigo 2x
# print('Seja bem vindo (a): %s' %nome)

# Print moderno
# print('Seja bem vindo {0}'.format(nome))

# Print mais atual
print(f'Seja Bem vindo(a) {nome}')

print('Informe sua idade: ')
idade = int(input())

# Input () -> Todo dado recebido via input é do tipo String.
# Por isso é necessário que se faça o cast, ou seja, a conversão
# dos dados.
print(f'{nome} você tem: {idade} anos')
print('++++++')

# FORMA MAIS ELEGANTE E USUAL DE RECEBER OS DADOS
nome2 = input('Qual nome da sua cidade?')
data  = int(input('Qual ano do seu nascimento?'))

print(f'Seu nome: {nome} e ano do seu nascimento: {data}')


