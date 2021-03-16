# Adicionando produtos num carrinho.
carrinho = []
produto = ''

while produto != 'Sair':
    produto = str(input('Adicione um produto na lista ou digite "sair" para sair.\n'
                        'Digite aqui: ')).strip().capitalize()
    if produto != 'Sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)