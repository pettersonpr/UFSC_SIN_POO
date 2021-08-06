num_matrizes = int(input())

def verificaMatriz3x3(lin, col):
    elementos = set()
    for l in range(lin, lin+3):
        for c in range(col, col+3):
            elementos.add(matriz[l][c])
    return len(elementos) == 9

for a in range(num_matrizes):
    matriz = []
    # criar matriz sudoku
    for _ in range(9):
        matriz.append([int(w) for w in input().split()])

    eh_solucao = 'SIM'
    # verificar linhas e colunas 9x9
    for i in range(9):
        if len(set(matriz[i])) != 9:
            eh_solucao = 'NAO'
            break
        # criar lista de colunas 9x9
        elementos = set()
        for j in range(9):
            elementos.add(matriz[j][i])
        # verificar coluna 9x9
        if len(elementos) != 9:
            eh_solucao = 'NAO'
            break

    if eh_solucao == 'SIM':
        parar = False
        for l in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not verificaMatriz3x3(l, c):
                    eh_solucao = 'NAO'
                    parar = True
                    break
            if parar:
                break
    print('Instancia {} \n{}'.format(a+1, eh_solucao))
