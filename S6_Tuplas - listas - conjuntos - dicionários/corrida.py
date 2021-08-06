num_carros, num_voltas = [int(w) for w in input().split()]
tempos = []
for i in range(num_carros):
    tempos.append(sum([int(x) for x in input().split()]))
tempos_copia = tempos.copy()
tempos_copia.sort()

for tempo in tempos_copia[0:3]:
    print(tempos.index(tempo)+1)

''' # Outra maneira de resolver
num_carros, num_voltas = [int(w) for w in input().split()]
tempos = []
for i in range(num_carros):
    tempos.append(sum([int(x) for x in input().split()]))

for _ in range(3):
    tempo = min(tempos)
    ind = tempos.index(tempo)
    print(ind+1)
    tempos[ind] = float('inf')
'''