
n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um número: '))
    if n !=0:
        if n % 2 == 0:
            par  = par + 1
        elif n % 2 == 1:
            impar = impar + 1

print(f'Números pares: {par}\n'
      f'Números impares: {impar}')