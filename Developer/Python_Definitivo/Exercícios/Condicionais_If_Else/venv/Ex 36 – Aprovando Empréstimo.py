# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

ValorCasa = float(input('Informe qual valor da casa que deseja comprar: '))
Salario = float(input('Informe seu salário: '))
Qtd_Parcelas = int(input('Informe a quantidade de parcelas que deseja financiar: '))
Valor_Parcelas = (ValorCasa/Qtd_Parcelas)
Mensalidade = (30/100) * Salario

if Valor_Parcelas > Mensalidade:
    print('Empréstimo NEGADO.')
    print(f'Valor das parcelas: R$ {Valor_Parcelas},00. Quanto você pode pagar por mês: R$ {Mensalidade},00')
else:
    print('Empréstimo ACEITO')
    print(f'Valor das parcelas: R$ {Valor_Parcelas},00.\n'
          f'Quantidade de parcelas: {Qtd_Parcelas} parcelas.\n'
          f'Quanto você pagará por mês: R$ {Mensalidade}, 00')
