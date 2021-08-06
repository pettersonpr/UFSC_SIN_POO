num_calouros = int(input())
lista_calouros = [input() for _ in range(num_calouros)]

num_doadores = int(input())
lista_doadores = [input() for _ in range(num_doadores)]

qtdd_calouros_doadores = 0

for calouro in lista_calouros:
    if calouro in lista_doadores:
        qtdd_calouros_doadores += 1

proporcao_calouros_doadores = qtdd_calouros_doadores / num_calouros

print(proporcao_calouros_doadores)
