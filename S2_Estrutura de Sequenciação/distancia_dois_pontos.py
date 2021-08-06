from math import *

# 1. Pegar valor dos pontos 1 e 2
x1, y1 = [float(w) for w in input().split()]
x2, y2 = [float(w) for w in input().split()]

# 2. Calcular distancia entre os pontos
distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 3. Imprimir valor
print("{:.4f}".format(distancia))
