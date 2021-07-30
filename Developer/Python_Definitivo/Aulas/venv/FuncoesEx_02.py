def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos +=1


valores = [6, 3, 1, 0, 12]
dobra(valores)
print(valores)