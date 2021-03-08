#for c in range(0,3):
 #   int(input('Digite um número: '))
#print('FIM')


soma = 0
for i in range(0,5): # Somou do 0 ao 4. Parou no 5.
    soma = soma + i
    print(soma)

print('----')

s = 0
for c in range(0,4):
    x = int(input('Digite um valor: '))
    s = s + x

print(f'Soma dos valores contidos em "s": {s}\n'
      f'Quantas vezes foram somados: {c+1}')