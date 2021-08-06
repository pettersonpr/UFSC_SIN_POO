import math
# Entrada
n = int(input())

limite_inferior = n / math.log(n)
limite_superior = limite_inferior * 1.25506

print("{:.1f} {:.1f}".format(limite_inferior, limite_superior))
