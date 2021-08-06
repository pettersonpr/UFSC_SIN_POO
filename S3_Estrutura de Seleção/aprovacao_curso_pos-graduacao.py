def equivalente_num(conceito):
    if conceito == 'A':
        eqv = 4
    elif conceito == 'B':
        eqv = 3
    elif conceito == 'C':
        eqv = 2
    else:
        eqv = 0
    return eqv


c1 = input()
c2 = input()
c3 = input()
c4 = input()

ia = (equivalente_num(c1) + equivalente_num(c2) + equivalente_num(c3) + equivalente_num(c4)) / 4
esta_aprovado = ia >= 3 and c1 != 'E' and c2 != 'E' and c3 != 'E' and c4 != 'E'
print(esta_aprovado)
