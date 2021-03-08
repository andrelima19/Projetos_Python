#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

Lado_A = float(input('Informe o lado "A" do triÂngulo: '))
Lado_B = float(input('Informe o lado "B" do triÂngulo: '))
Lado_C = float(input('Informe o lado "C" do triÂngulo: '))

# if Lado_A == Lado_B and Lado_B == Lado_C:
    #print('Triângulo Equilátero.')

#elif (Lado_A == Lado_B and Lado_A != Lado_C) or (Lado_C == Lado_A and Lado_C != Lado_B)\
     #   or (Lado_B == Lado_A and Lado_B != Lado_C) or (Lado_B == Lado_C and Lado_C != Lado_A):
    # print('Triângulo Isósceles.')

#elif Lado_A != Lado_B and Lado_B != Lado_C and Lado_A != Lado_C:
 #   print('Triângulo Escaleno')

if Lado_A == Lado_B == Lado_C:
    print('Triângulo Equilátero.')
elif Lado_A != Lado_B != Lado_C != Lado_A:
    print('Triângulo Escaleno')
else:
    print('Triângulo Isósceles')

