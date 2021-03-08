# Exercício Python 14: Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

# Fórmula: (0 °C × 9/5) + 32 = 32 °F

celsius = float(input('Informe a temperatura em Celsius: '))
fahrenheit = celsius * (9/5) + 32

print(f'Temperatura em graus Celsius: {celsius}\n'
      f'Temperatura em graus fahrenheit: {fahrenheit}')
