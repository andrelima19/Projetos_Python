# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

"A"
# Quantas vezes aparece;
# Em que posição aparece a primeira vez;
# Em que posição aparece a última vez

frase = str(input('Digite uma frase: ')).strip() # strip pra eliminar os espaços inuteis e
      # evitar erros.

print(f'Número de vezes: {frase.count("A")}\n'
      f'A letra "A" aparece na posição: {frase.find("A")} pela primeira vez\n' 
      f'A letra "A" aparece na posição: {frase.rfind("A")} pela última vez')
