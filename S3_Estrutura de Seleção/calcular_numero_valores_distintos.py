'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

soma = (a==b) + (a==c) + (a==d) + (b==c) + (b==d) + (c==d)

if soma == 6:
    distintos = 1
elif soma == 0:
    distintos = 4
elif soma == 1:
    distintos = 3
else:
    distintos = 2

print(distintos)'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

distintos = 4

if a==b or a==c or a==d:
    distintos -= 1
if b==c or b==d:
    distintos -= 1
if c==d:
    distintos -= 1

print(distintos)
