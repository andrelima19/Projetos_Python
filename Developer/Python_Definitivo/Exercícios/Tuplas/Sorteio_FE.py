# Sorteio das qualidades do Fruto do Espírito

import random
resp = ''

qualidades = ['amor', 'alegria', 'paz', 'paciência', 'bondade', 'benignidade', 'fé']
random.shuffle(qualidades)

print('Qualidades do fruto do Espírito: '
      'amor, alegria, paz, paciência, bondade, benignidade, fé')

while resp in 'sim':
    resp = str(input('Deseja continuar? ')).strip().lower()
    qualidades.pop(0)
    print(qualidades)

    if qualidades == []:
        break
print('FIM')
