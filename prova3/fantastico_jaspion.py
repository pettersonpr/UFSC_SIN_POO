num_instancia = int(input())

for _ in range(num_instancia):
    num_palavras, num_linhas = [int(w) for w in input().split()]
    dicionario_jap_port = []
    for i in range(num_palavras):
        dicionario_jap_port.append([input(), input()])
    d_jap_port = dict(dicionario_jap_port)
    for _ in range(num_linhas):
        frase = input().split()
        for palavra in frase:
            if palavra in d_jap_port.keys():
                frase[frase.index(palavra)] = d_jap_port[palavra]
        print(' '.join(frase))
    print()
