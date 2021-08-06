'''origem_escala = input()
temperatura = float(input())
destino_escala = input()

if origem_escala == 'c':
    if destino_escala == 'f':
        print(temperatura * 1.8 + 32)
    elif destino_escala == 'k':
        print(temperatura + 273.15)
    else:
        print((temperatura + 273.15) * 1.8)

elif origem_escala == 'f':
    if destino_escala == 'c':
        print((temperatura-32)/1.8)
    elif destino_escala == 'k':
        print((temperatura+459.67)/1.8)
    else:
        print(temperatura+459.67)

elif origem_escala == 'k':
    if destino_escala == 'c':
        print(temperatura-273.15)
    elif destino_escala == 'f':
        print(temperatura*1.8-459.67)
    else:
        print(temperatura*1.8)

else:
    if destino_escala == 'c':
        print((temperatura-32-459.67)/1.8)
    elif destino_escala == 'f':
        print(temperatura-459.67)
    else:
        print(temperatura/1.8)
'''
