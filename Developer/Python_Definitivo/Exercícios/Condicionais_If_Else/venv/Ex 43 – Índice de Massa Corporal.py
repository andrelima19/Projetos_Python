# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#
# IMC = Peso ÷ (Altura × Altura)

# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida

from math import pow

peso  = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (pow(altura,2))

if imc <= 18.5:
    print(f'IMC: {imc:.2f} - Abaixo do peso.')

elif imc >18.5 and imc <= 25:
    print(f'IMC: {imc: .2f} - Peso ideal.')

elif imc >25 and imc <= 30:
    print(f'IMC: {imc: .2f} - Sobrepeso')

elif imc >30 and imc <= 40:
    print(f'IMC: {imc: .2f} - Obesidade')

else:
    print(f'IMC: {imc: .2f} - Obesidade Mórbida')