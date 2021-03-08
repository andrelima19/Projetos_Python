# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Informe a distância percorrida: '))

if distancia <= 200:
    print(f'Preço da viagem: {distancia * 0.5}')
else:
    print(f'Preço da viagem: {distancia * 0.45}')