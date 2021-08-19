'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

def voto(data):
    from datetime import date
    data_hoje = date.today().year
    idade = data_hoje - data

    if idade < 16:
        resp = f'Você não pode votar. Sua idade: {idade}'
        return resp

    elif idade >=16 and idade< 18:
        resp = f'Voto opcional. Sua idade é: {idade}'
        return resp

    else:
        resp = f'Voto obrigatório. Sua idade é: {idade}'
        return resp

data = int(input('Informe o ano em que você nasceu: '))
print(voto(data))