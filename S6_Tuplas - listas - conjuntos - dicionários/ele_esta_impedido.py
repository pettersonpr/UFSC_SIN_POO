num_atacantes, num_defensores = [int(i) for i in input().split()]

while num_atacantes != 0 and num_defensores != 0:
    distancia_atacantes = [int(i) for i in input().split()]
    distancia_defensores = [int(i) for i in input().split()]
    distancia_atacantes.sort()
    distancia_defensores.sort()
    if distancia_atacantes[0] < distancia_defensores [1]:
        print('Y')
    else:
        print('N')
    num_atacantes, num_defensores = [int(i) for i in input().split()]
