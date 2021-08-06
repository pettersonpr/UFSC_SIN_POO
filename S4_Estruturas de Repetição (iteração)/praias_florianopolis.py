qtdd_praias = int(input())
maior_distancia = 0
qtdd_15_20 = 0
soma_distancia = 0

for _ in range(qtdd_praias):
    praia, distancia = input().split(';')
    distancia = int(distancia)

    if distancia > maior_distancia:
        maior_distancia = distancia
        praia_mais_distante = praia
    if 15 <= distancia <= 20:
        qtdd_15_20 += 1
    soma_distancia += distancia

media_distancia = soma_distancia / qtdd_praias

print('{};{};{:.1f}'.format(praia_mais_distante, qtdd_15_20, media_distancia))
