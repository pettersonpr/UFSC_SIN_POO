num_saltadores = int(input())
maior_salto_geral = 0

for _ in range(num_saltadores):
    s1, s2, s3, saltador = [x for x in input().split()]
    s1 = float(s1)
    s2 = float(s2)
    s3 = float(s3)

    maior_salto_saltador = max(s1, s2, s3)

    if maior_salto_saltador > maior_salto_geral:
        maior_salto_geral = maior_salto_saltador
        melhor_saltador = saltador

print(melhor_saltador)
