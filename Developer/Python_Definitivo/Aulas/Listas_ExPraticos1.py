'''
num = (1,2,4,9,5)
num[2] = 1 #Mudando o valor numa tupla - ERRO.
print(num)
'''
num = [1,3,2,4,9,5]
print(num)

num[2] = 1 #Mudando o valor numa lista.
print(num)

num.append(11)# Adicionando valor
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.insert(3,24)
print(num)

print(f'A lista tem: {len(num)} valores')

num.pop()
print(num)

num.pop(3)
print(num)

num.remove(4)
print(num)