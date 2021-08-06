# Rever código

vx1, vy1, vx2, vy2 = [int(x) for x in input().split()]
ax1, ay1, ax2, ay2 = [int(x) for x in input().split()]

tem_interseccao = 1

if ax1 > vx2 or ax2 < vx1 or ay1 > vy2 or ay2 < vy1:
    tem_interseccao = 0

print(tem_interseccao)
