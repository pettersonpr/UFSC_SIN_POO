# Pegando valor
xicara, ovos, colher = [int(w) for w in input().split()]

'''
    Descobrindo quociente inteiro que indicará a quantidade máxima de bolos 
    para cada ingrediente. Depois disso só pegar o menor valor para descobrir a
    quantidade de bolos que poderá ser feito com ambos os ingredientes juntos.
'''
# Calculando quociente inteiro dos ingrediente
xicara = xicara // 2
ovos = ovos // 3
colher = colher // 5

# Quantidade de bolos
bolos = min(xicara, ovos, colher)

# Saída
print(bolos)
