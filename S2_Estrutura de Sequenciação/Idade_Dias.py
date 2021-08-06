idade = int(input())

# Verificar idade em anos, meses e dias
anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30

print(anos, meses, dias)
