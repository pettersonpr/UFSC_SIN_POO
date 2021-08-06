num = float(input())

if num > 0:
    num = '+' + format(num, ".4E")
elif num < 0:
    num = format(num, ".4E")

print(num)
