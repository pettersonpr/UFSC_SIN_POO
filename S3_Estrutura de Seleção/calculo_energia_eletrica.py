kwh = int(input())

acima_200 = max(0, kwh - 200)
valor = acima_200 * 0.27836
kwh -= acima_200

acima_100 = max(0, kwh - 100)
valor += acima_100 * 0.25052
kwh -= acima_100

acima_30 = max(0, kwh - 30)
valor += acima_30 * 0.16698
kwh -= acima_30

valor = round(valor + kwh * 0.09556, 2)

print(valor)
