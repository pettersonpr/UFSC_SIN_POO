n = int(input())
m = int(input())

'''for i in range(1, m+1, 1):
    if i % n == 0:
        print(i, end=" ")'''

for i in range(n, m+1, n):
    print(i, end=" ")
