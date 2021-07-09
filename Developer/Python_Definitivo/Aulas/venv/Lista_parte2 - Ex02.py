galera = []
dado = []
maior_idade = 0
menor_idade = 0

for c in range(0,4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >=18:
        print(f'{p[0]} é maior de idade.')
        maior_idade +=1
    else:
        print(f'{p[0]} é menor de idade:')
        menor_idade +=1

print(f'A quantidade pessoas maior de idade é: {maior_idade}\n'
      f'A quantidade de pessoas menor de idade é: {menor_idade}')