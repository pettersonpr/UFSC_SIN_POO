# Entrada
A, B, C = [int(w) for w in input().split()]
X, Y, Z = [int(w) for w in input().split()]

# Calcular quantidade
qtddX = X // A
qtddY = Y // B
qtddZ = Z // C

quantidadeConteiner = qtddX * qtddY * qtddZ

# Saída
print(quantidadeConteiner)
