n = int(input())
p = 1
q = 1

x = 1
for _ in range(3, n+1):
    x = p + q
    p = q
    q = x

print(x)
