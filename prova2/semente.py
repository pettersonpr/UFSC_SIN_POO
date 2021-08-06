comprim_fita, num_gotas = [int(w) for w in input().split()]
posicao_gotas = [int(w) for w in input().split()]
fita_com_gotas = [0] * comprim_fita

for i in range(num_gotas):
    fita_com_gotas[posicao_gotas[i] - 1] = 1

dias = 0

while 0 in fita_com_gotas:
    dias += 1
    copia_fita = fita_com_gotas.copy()
    for i in range(comprim_fita):
        if fita_com_gotas[i] == 1:
            if i != 0 and i != comprim_fita - 1:
                copia_fita[i - 1] = 1
                copia_fita[i + 1] = 1
            elif i == 0:
                copia_fita[i + 1] = 1
            else:
                copia_fita[i - 1] = 1
    fita_com_gotas = copia_fita

print(dias)
