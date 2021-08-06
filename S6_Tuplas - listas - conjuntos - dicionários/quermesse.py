num_participantes = int(input())
lista_ganhadores = []

while num_participantes != 0:
    ordem_entrada = [int(w) for w in input().split()]
    for i in range(len(ordem_entrada)):
        if i + 1 == ordem_entrada[i]:
            lista_ganhadores.append(ordem_entrada[i])
    num_participantes = int(input())

for i in range(len(lista_ganhadores)):
    print('Teste {} \n {}'.format(i+1, lista_ganhadores[i]), '\n')
