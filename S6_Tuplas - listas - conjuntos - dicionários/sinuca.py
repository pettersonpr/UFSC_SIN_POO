n = int(input())
bolas = [int(i) for i in input().split()]

t = n - 1
for k in range(n-1):
    for i in range(t):
        if bolas[i] == bolas[i+1]:
            bolas[i] = 1
        else:
            bolas[i] = - 1
    t -= 1

if bolas[0] == 1:
    print("preta")
else:
    print("branca")
