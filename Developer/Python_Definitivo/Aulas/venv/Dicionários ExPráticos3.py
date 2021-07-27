brasil = []
estado = {}

for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

print(brasil)

for e in brasil:
    print(e)

# Outra forma
for e in brasil:

    for k, v in e.items():
        print(f'O campo {k} tem valor: {v}.')