dias_usados = int(input())
km = float(input())

if km > dias_usados * 60:
    excedente_km = (km - dias_usados * 60) * 0.5
    print(dias_usados * 45 + excedente_km)
else:
    print(dias_usados * 45)
