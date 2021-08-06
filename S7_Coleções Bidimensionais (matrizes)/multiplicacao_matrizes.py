N = int(input())
P, Q, R, S, X, Y = [int(w) for w in input().split()]
i, j = [int(w) for w in input().split()]

cij = 0  # A(i, k) * B(k j) = C(i, j)
for k in range(1, N+1):
    cij += ((P * i + Q * k) % X) * ((R * k + S * j) % Y)

print(cij)
