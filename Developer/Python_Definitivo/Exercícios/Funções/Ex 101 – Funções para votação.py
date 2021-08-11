'''
Exercício 101 – Funções para votação
Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
import datetime
from datetime import date


def voto():
    # Exibindo a data atual
    data_atual = datetime.datetime.now()
    data = data_atual.date()
    data_atual = data.year

    resp = int(input('Informe o ano do seu nascimento: '))
    valid = (data_atual - resp)

    if valid < 16:
        print(f'Sua idade é: {valid} anos você não pode votar!')

    elif valid >= 16 and valid < 18:
        print(f'Sua idade é: {valid} anos seu voto é opcional!')

    else:
        print(f'Sua idade é: {valid} anos você pode votar!')

voto()