'''tamanho_chocolate = int(input())
quantidade_pedacos = 1

while tamanho_chocolate >= 2:
    tamanho_chocolate /= 2
    quantidade_pedacos *= 4

print(quantidade_pedacos)
'''

import math

lado = int(input())
num_divisoes = math.log(lado, 2)
num_pedacos = 4 ** num_divisoes
print(num_pedacos)

