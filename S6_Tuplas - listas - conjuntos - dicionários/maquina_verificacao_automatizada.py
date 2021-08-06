conector_1 = [int(w) for w in input().split()]
conector_2 = [int(w) for w in input().split()]

compativeis = 'Y'
for i in range(5):
    if conector_1[i] == conector_2[i]:
        compativeis = 'N'
        break

print(compativeis)
