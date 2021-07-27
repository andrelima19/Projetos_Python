pessoas = {'nome': 'André', 'sexo': 'M', 'idade':32}
print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for i in pessoas.items():
    print(i)

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
print(pessoas)

# Modificando um valor
pessoas['nome'] = 'Mario'
print(pessoas)

# Adicionando uma key
pessoas['peso'] = 98.3

print(pessoas)