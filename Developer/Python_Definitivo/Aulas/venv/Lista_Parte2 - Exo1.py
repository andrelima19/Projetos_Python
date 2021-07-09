teste = []
teste.append('Gustavo')
teste.append(40)

galera = []
galera.append(teste[:])
teste[0] = 'André'
teste[1] = 32
galera.append(teste[:])

print(galera)

#########################3
turma = [['Jaime', 11], ['Marcelo', 12], ['Bia', 10], ['Gabi', 11]]
print(turma)
print(turma[1][1])

for p in turma:
    print(p)
    print(f'Nome:{[0]} -- Idade: {[1]}')

