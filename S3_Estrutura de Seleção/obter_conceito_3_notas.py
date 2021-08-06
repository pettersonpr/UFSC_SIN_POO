nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1+nota2+nota3) / 3

if media >= 9:
    conceito = 'Ótimo'
elif media >= 7.5:
    conceito = 'Bom'
elif media >= 6:
    conceito = 'Satisfatório'
else:
    conceito = 'Isatisfatório'

print(conceito)
