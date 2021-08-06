quadro_aulas = [
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
]
horarios_indice = {'0730': 0, '0820': 1, '1010': 2, '1100': 3, '1330': 4, '1420': 5, '1510': 6, '1620': 7, '1710': 8, '1830': 9, '1920': 10, '2020': 11, '2110': 12}
disciplinas_choque = ''
qtdd_disciplinas = int(input())

for _ in range(qtdd_disciplinas):
    aulas = [w for w in input().split()]
    # percorrer a lista com horarios dhhmmn
    for horario in aulas[1:]:
        d_semana = int(horario[0]) # SEG = 2, TER = 3 ..., SAB = 7
        hhmm = horarios_indice[horario[1:5]]  # retorna o índice relativo ao horário
        n_aulas = int(horario[5])
        contador = 0
        for _ in range(n_aulas):
            if quadro_aulas[hhmm + contador][d_semana] == '':
                quadro_aulas[horarios_indice[horario[1:5]] + contador][int(horario[0])] = aulas[0]
            else:
                disciplinas_choque = disciplinas_choque + quadro_aulas[hhmm + contador][d_semana] + ' ' + aulas[0]
                #print(quadro_aulas[hhmm + contador][d_semana], ' ', aulas[0])
                break
            contador += 1
print(disciplinas_choque[:15])
