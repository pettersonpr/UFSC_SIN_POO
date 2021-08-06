import numpy as np

num_linhas, num_colunas = [int(w) for w in input().split()]
m = []
for _ in range(num_linhas):
    m.append([int(w) for w in input().split()])


def maior_num(m):
    row = max(np.sum(m, axis=1))
    column = max(np.sum(m, axis=0))
    return max(row, column)


print(maior_num(m))
