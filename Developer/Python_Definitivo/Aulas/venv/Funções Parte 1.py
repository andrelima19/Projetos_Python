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
    print('=' * 30)


# programa principal
lin() # O comando só é executado quando a função é chamada.
print('André')
print('Curso Em vídeo')
lin()

'''FUNÇÃO COM PARÂMETROS'''
def mensagem(msg):
    print('=' * 30)
    print(msg)
    print('=' * 30)

mensagem('André') # o conteúdo do argumento é passado a variável 'msg'
mensagem('Lima')
mensagem('Casa')