import math
n = int(input())

#Começar com o maior valor +infinito
primeiro_menor = math.inf
print(primeiro_menor)
segundo_menor = math.inf
for _ in range(n):
    x = int(input())
    if x < primeiro_menor:
        segundo_menor = primeiro_menor
        primeiro_menor = x
    elif x < segundo_menor:
        segundo_menor = x

print(segundo_menor)
