
dados1 = dict()
dados = {'Nome': 'Pedro', 'Idade': 23}

#Exibindo elementos
#Exibindo todos os elementos
print(dados)

#Exibindo um elemento
print(dados['Nome'])

# Adicionando elementos
dados ['Sexo'] = 'M'

print(dados)

#Removendo elementos
del dados['Idade']
print(dados)

filme={'titulo': 'Star Wars', 'ano':1977, 'director': 'George Lucas'}
print(filme.values()) # Exibe apenas o valor
print(filme.keys()) # Exibe apenas o 'indíce'
print(filme.items()) # Exibe todos os itens que compoe o dicionário'

# Usando como Enumerate

for K, v in filme.items():
    print(f'O {K} é {v}')

# Combinando com Listas

# Passando uma lista para um dic

turma = {}
aluno = []

turma['aluno'] = aluno # Dicionário recebe a lista criada
aluno.append('André') # Lista recebe valor.
print(turma)


dic = {}
lista = []
dic['a'] = lista
lista.append('a')
print(dic)