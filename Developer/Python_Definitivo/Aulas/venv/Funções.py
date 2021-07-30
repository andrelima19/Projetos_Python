'''
FUNÇÃO
'''
'''
Função - Rotina de programação - Algo feito constantemente
DEF é Definição de Função

'''
'''
Exemplo 1 
'''
def lin():
    print('-' * 30)

lin() # O comando só é executado quando a função é chamada.
print('Curso em Vídeo')
lin()
print('Aprenda Python')
lin()
print('André Lima')
lin()

'''
Exemplo 2 - Passando um parâmetro
'''
def mensagem(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

mensagem('Testando funções 1')
mensagem('Testando funções 2')
mensagem('Testando funções 3')
