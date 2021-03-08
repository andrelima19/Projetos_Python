# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o salário: '))

if salario > 1250:
    aumento = (salario) * 10/100
    print(f'Seu aumento foi de: R$ {aumento},00\n'
          f'Seu novo salário é: R${(salario + aumento)},00')
else:
    aumento = (salario * 15/100)
    print(f'Seu aumento foi de: R$ {aumento},00\n'
          f'Seu novo salário é: R${(salario + aumento)},00')