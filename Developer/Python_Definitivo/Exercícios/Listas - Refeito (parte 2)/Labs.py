
grupo_pessoas = []
dados = []
resp = ''
maior = menor = 0
pesado = leve = []

while True:
    n = str(input('Nome: '))
    dados.append(n)
    n = int(input('Peso: '))

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if 'S' not in resp:
        break

    if len(dados[1]) == 0:
        dados[1] = maior = menor
    else:
        if dados[1] > maior:
            pesado.append(dados[1])
        if dados[1] < menor:
            leve.append(dados[1])

print(pesado)
print(leve)