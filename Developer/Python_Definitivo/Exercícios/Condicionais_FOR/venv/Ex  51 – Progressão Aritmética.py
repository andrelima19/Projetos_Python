# Exercício Python 51: Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))

for c in range(1, 10):
    an = a1 + (c) * r
    print(f'Termo: {c} - PA: {an}')

print('===============')
print('Outra forma de se fazer.')

# Outra forma de se fazer.

primeiro = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
decimo = primeiro + (10 - 1) * razao
i = 0
for c in range (primeiro, decimo + razao, razao):
    i = i + 1
    print(f'Termo: {i} - PA: {c}')