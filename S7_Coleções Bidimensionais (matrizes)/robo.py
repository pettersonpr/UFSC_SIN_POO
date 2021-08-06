num_linhas, num_colunas = [int(w) for w in input().split()]
x_inicial, y_inicial = [int(w) for w in input().split()]

matrix = []
for _ in range(num_linhas):
    matrix.append([int(w) for w in input().split()])

response = ()

x_inicial -= 1
y_inicial -= 1
x_anterior = 0
y_anterior = 0
while not response:
    count = 0
    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni = x_inicial + di
        nj = y_inicial + dj
        if 0 <= ni < num_linhas and 0 <= nj < num_colunas and matrix[ni][nj] == 1 and (ni, nj) != (x_anterior, y_anterior):
            count = 0
            x_anterior = x_inicial
            y_anterior = y_inicial
            x_inicial = ni
            y_inicial = nj
        else:
            count += 1
    if count == 4:
        response = (x_inicial + 1, y_inicial + 1)
print(' '.join(str(response)))
