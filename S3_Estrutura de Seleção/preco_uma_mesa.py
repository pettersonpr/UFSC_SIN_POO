comprimento = float(input())
largura = float(input())
num_favetas = int(input())
tipo_madeira = input()


preco = (comprimento * largura * 100) + num_favetas * 30
if tipo_madeira == 'mogno':
    preco += 150
elif tipo_madeira == 'carvalho':
    preco += 125
if largura * comprimento > 2:
    preco += 50
if preco < 200:
    preco = 200
print('{}'.format(preco))
