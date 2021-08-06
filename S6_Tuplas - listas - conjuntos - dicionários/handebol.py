num_jogadores, num_partidas = [int(i) for i in input().split()]
gols_todas_partidas = 0

for i in range(num_jogadores):
    gols_jogos = [w for w in input().replace(' ','')]
    if '0' not in gols_jogos:
        gols_todas_partidas += 1
print(gols_todas_partidas)
