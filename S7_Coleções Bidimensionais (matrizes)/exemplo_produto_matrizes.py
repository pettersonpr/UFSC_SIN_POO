def multiplica_matrizes(a, b):
    """ Multiplica duas matrizes a(m,n) e b(n,p), retornando c(m,p) """
    m = len(a)  # o número de linhas de a
    n = len(b)  # o número de linhas de b
    p = len(b[0])  # o número de colunas de b

    c = []  # inicia com uma matriz vazia
    for i in range(m):
        c.append([0] * p)
        for j in range(p):
            soma = 0
            for k in range(n):
                soma += a[i][k] * b[k][j]
            c[i][j] = soma

    return c


A = [[1, 2, 3],
     [3, 4, 3]
     ]
B = [[1]
     ]
C = multiplica_matrizes(A, B)

print(C)
