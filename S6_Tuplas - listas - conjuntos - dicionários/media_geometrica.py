qtdd = int(input())

produto = 1

for i in range(qtdd):
    valor = float(input())
    produto *= valor
raiz_enesima = produto ** (1 / qtdd)
print(raiz_enesima)
