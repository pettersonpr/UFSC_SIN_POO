num_perguntas, qtdd_frequencia = [int(w) for w in input().split()]
lista_perguntas = [int(w) for w in input().split()]

contador = 0

while num_perguntas != 0 and qtdd_frequencia != 0:
    for i in range(1, num_perguntas+1):
        if lista_perguntas.count(i) >= qtdd_frequencia:
            contador += 1
    print(contador)
    num_perguntas, qtdd_frequencia = [int(w) for w in input().split()]
    lista_perguntas = [i for i in input().split()]
