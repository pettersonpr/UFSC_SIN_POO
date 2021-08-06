num_pessoas = int(input())

while num_pessoas != 0:
    tempos_entradas = [int(w) for w in input().split()]
    tempo_escada_ativa = num_pessoas * 10
    if num_pessoas > 1:
        for i in range(num_pessoas - 1):
            if (tempos_entradas[i] + 10) > tempos_entradas[i+1]:
                tempo_escada_ativa -= (tempos_entradas[i] + 10) - tempos_entradas[i+1]
    print(tempo_escada_ativa)
    num_pessoas = int(input())
