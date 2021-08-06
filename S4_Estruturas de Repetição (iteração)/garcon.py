bandejas = int(input())
copos_quebrados = 0

for _ in range(bandejas):
    latas, copos = [int(w) for w in input().split()]
    if latas > copos:
        copos_quebrados += copos

print(copos_quebrados)
