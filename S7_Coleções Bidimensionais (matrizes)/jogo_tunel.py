while True:
    try:
        num_linhas, num_colunas = [int(w) for w in input().split()]

        m = []
        for _ in range(num_linhas):
            m.append([w for w in input().split()])

        i = 0
        j = m[i].index('X')
        anterior_i = -1
        anterior_j = -1

        direcao = 'D'
        coordenadas_dic = {(0, 1): 'R', (0, -1): 'L', (1, 0): 'U', (-1, 0): 'D'}
        coordenadas = []
        while (True):
            count = 0
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni = i + di
                nj = j + dj
                if 0 <= ni < num_linhas and 0 <= nj < num_colunas and m[ni][nj] == '0' and (ni, nj) != (anterior_i, anterior_j):
                    if direcao == 'D':
                        coordenadas_dic[(0, 1)] = 'L F'
                        coordenadas_dic[(0, -1)] = 'R F'
                        coordenadas_dic[(1, 0)] = 'F'
                        coordenadas_dic[(-1, 0)] = 'F'
                    if direcao == 'R':
                        coordenadas_dic[(0, 1)] = 'F'
                        coordenadas_dic[(0, -1)] = 'F'
                        coordenadas_dic[(1, 0)] = 'R F'
                        coordenadas_dic[(-1, 0)] = 'L F'
                    if direcao == 'L':
                        coordenadas_dic[(0, 1)] = 'F'
                        coordenadas_dic[(0, -1)] = 'F'
                        coordenadas_dic[(1, 0)] = 'L F'
                        coordenadas_dic[(-1, 0)] = 'R F'
                    if direcao == 'U':
                        coordenadas_dic[(1, 0)] = 'F'
                        coordenadas_dic[(-1, 0)] = 'F'

                    coordenadas.append(coordenadas_dic[(di, dj)])
                    coordenadas_dic = {(0, 1): 'R', (0, -1): 'L', (1, 0): 'D', (-1, 0): 'U'}
                    direcao = coordenadas_dic[(di, dj)]
                    count = 0
                    anterior_i = i
                    anterior_j = j
                    i = ni
                    j = nj
                else:
                    count += 1
            if count == 4:
                coordenadas.append('E')
                break

        print(*coordenadas)
    except EOFError:
        break
