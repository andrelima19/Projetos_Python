"""
Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(),
upper(), lower(), capitalize(), title(), strip(), junção com join().
"""
# Fatiamento de Strings

frase = str('O rato roeu a roupa do rei de roma.')
print(frase[3]) # Retorna o carctere da posição 3 da lista []

print(frase[3:11]) # Retorna o carctere da posição 3 até a posição 11 da lista []
print(frase[3:10:2])# Retorna o carctere da posição 3 até a posição 11 da lista [] pulando de 2 em dois.
print(frase[:5]) # Começa do inicio (posição 0 e vai até a posição 5
print(frase[15:]) # Começa do 15 até o final (:) pois não sabe qual ultimo caractere
print(frase[9::3]) # Começa no indice 9 e vai até o final : . Começa do indíce que se torna o início e
# pula de 3 em 3.

# Análise de Strings
# len - Mostra a quantidade de caracteres
print(len(frase))

# count
print(frase.count('0')) # Conta quantas vezes aparece um caractere
print(frase.count('0', 0, 13)) # Entre a posição 0 e 13 mostre quantas vezes o carctere 'O' aparece.

# find
print(frase.find('ro')) # Mostra em que posição o caractere foi encontrado

# in
print('roma' in frase) # Existe a palavra 'roma' na varíavel frase?

# Transformação
# replace (Trocar)
print(frase.replace('roma', 'Paris'))

# upper
print(frase.upper()) # Toda frase em maiusculo

#lower
print(frase.lower())# Toda frase em minusculo

#capitalize
print(frase.capitalize()) # Os primeiros caracteres apenas em maiusculo

#title
print(frase.title()) # A primeira letra de cada palavra em Maiusculo

frase2 = str('     O rato roeu a roupa do rei de roma.   ')

#strip
print(frase2.strip()) # Remove todos os espaços inúteis.

#rstrip - Remove os últimos espaços da direita
print(frase2.rstrip()) # Remove todos os espaços inúteis.

#lstrip - Remove os últimos espaços da esquerda
print(frase2.lstrip()) # Remove todos os espaços inúteis.

#Divisão
#split
print(frase.strip()) # Gera uma lista com todas as palavras numa frase
# Divide uma string em uma lista

#join
print('-'.join(frase))# Junta os elementos de frase com qualquer caracterer ou sem carctere.




