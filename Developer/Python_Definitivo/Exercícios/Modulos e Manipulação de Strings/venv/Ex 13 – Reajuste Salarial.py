# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salário, com 15% de aumento.

Salario = float(input('Informe seu salário atual: '))
print(f'Salário atual R${Salario},00')

NovoSalario = (Salario + (Salario * 15/100))

print(f'Novo salário: R${NovoSalario},00')