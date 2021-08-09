
def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é : {fatorial(n)}')


def fatorial2(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

f1 = fatorial2(10)
f2 = fatorial2(3)
f3 = fatorial2()

print(f'Os resultados são: {f1}, {f2}, {f3}')

print()

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É Par!')
else:
    print('É impar!')