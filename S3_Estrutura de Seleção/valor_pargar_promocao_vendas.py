preco = float(input())

if preco >= 500:
    if preco > 1000:
        preco_pagar = preco - preco * 0.3 - (preco - 1000) * 0.15
    else:
        preco_pagar = preco - preco * 0.3
else:
    preco_pagar = preco - preco * 0.2

print('{:.2f}'.format(preco_pagar))
