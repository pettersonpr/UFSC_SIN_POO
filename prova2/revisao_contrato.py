dig_problema, num_negociado = [str(w) for w in input().split()]

while dig_problema != '0' and num_negociado != '0':
    num_sem_dig_problema = num_negociado.replace(dig_problema, '')
    if num_sem_dig_problema != '':
        print(int(num_sem_dig_problema))
    else:
        print(0)
    dig_problema, num_negociado = [str(w) for w in input().split()]
