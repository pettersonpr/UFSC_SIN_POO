linhas, colunas = [int(w) for w in input().split()]
matriz = []
indice_menor_valor = []

for i in range(linhas):
    matriz.append([int(w) for w in input().split()])
    indice_menor_valor.append(matriz[i].index(min(matriz[i])))


elementos_colunas = []
indices_finais = ''
for i in range(linhas):
    elementos_colunas = []
    for j in range(linhas):
        if j != i:
            elementos_colunas.append(matriz[j][indice_menor_valor[i]])
    if matriz[i][indice_menor_valor[i]] > max(elementos_colunas):
        indices_finais = str(i+1) + ' ' + str(indice_menor_valor[i]+1)

if indices_finais != '':
    print(indices_finais)
else:
    print(False)

