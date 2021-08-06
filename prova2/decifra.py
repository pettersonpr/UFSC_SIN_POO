alfabeto = 'abcdefghijklmnopqrstuvwxyz'
alfabeto_crip = input()
msg_crip = input()

indices = []
msg = ''
for letra in msg_crip:
    indices.append(alfabeto_crip.index(letra))
for i in indices:
    msg = msg + alfabeto[int(i)]
print(msg)
