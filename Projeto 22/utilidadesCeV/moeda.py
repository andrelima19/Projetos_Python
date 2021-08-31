
'''
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

def aumentar(valor = 0, taxa = 0, formato=False):
    '''
    Param valor
    Param taxa
    Param formato
    return
    '''
    aumento = (valor * taxa/100) + valor
    return aumento if formato is False else moeda(aumento)

def diminuir(valor = 0, taxa = 0, formato=False):
    reduzir = valor - (valor * taxa/100)
    return reduzir if formato is False else moeda(reduzir)

def dobro(valor=0, formato=False):
    dobrar = (valor*2)
    return dobrar if formato is False else moeda(dobrar)

def metade(valor, formato=False):
    meio = (valor/2)
    return meio if formato is False else moeda(meio)

def moeda(valor = 0, moeda = 'R$'):
    #formatacao = f'R$ {valor:.2f}'
    #return formatacao
    return f'{moeda}{valor:>.2f}'.replace('.', ',')

def resumo(preco=0, taxa=10, taxar=5):
    print('=' * 30)
    print('Resumo do Valor'.center(30))
    print('=' * 30)
    print(f'Preço analisado: {moeda(preco)}')
    print(f'Dobro do preço: {moeda(dobro(preco))}')
    print(f'Metade do valor: {moeda(metade(preco))}')
    print(f'Aumento de {taxa}%: {aumentar(preco, taxa, True)}')
    print(f'Redução de {taxar}%:  {diminuir(preco, taxar, True)}')

'''
x = int(input('Valor: R$'))
print(f'{moeda(x)}')
'''
