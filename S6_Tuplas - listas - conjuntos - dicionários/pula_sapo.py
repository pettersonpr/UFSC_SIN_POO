p, n = [int(x) for x in input().split()]

alturas = [int(x) for x in input().split()]

resultado = 'YOU WIN'
for i in range(0, n-1):
    if abs(alturas[i] - alturas[i+1]) > p:
        resultado = 'GAME OVER'
        break
print(resultado)
