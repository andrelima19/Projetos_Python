
''''''
'''TRATAMENTO DE EXCEÇÕES
Quando o erro não se dá de forma sintática,
ele vira uma exceção. (Dá-se o nome de)

É um erro que não ocorre sempre.

Como tratar as exceções?
>>> Clausulas <<<
Try (Onde será colocada a operação)
except (Se der erro)
else: (deu certo)
finally: (certo/falha)
'''

'''1º forma'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except:
    print('ERRO')
else:
    print(f'O resultado é: {r:.1f}')


'''2º forma - Usando um alias para a classe Exception'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__class__}')
else:
    print(f'O resultado é: {r:.1f}')

'''3º forma - Usando um alias para a classe Exception e usando a clausula: Finally '''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__class__}')
else:
    print(f'O resultado é: {r:.1f}')
finally:
    print('Volte sempre! Obrigado!')