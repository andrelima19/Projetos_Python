
maior = menor = 0
cont = 0
peso = 0

for c in range(0,3):
    peso = int(input('Peso: '))

    c +=1
    if c == 1:
        maior = menor = peso
    else:
         if peso > maior:
              maior = peso
         if peso < maior:
              menor = peso

print(f'Maior: {maior} e Menor: {menor}')