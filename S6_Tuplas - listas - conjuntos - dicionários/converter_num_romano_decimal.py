valores_romanos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
num_romano = input()

decimal = 0
for i in range(len(num_romano)-1):  # Exclui o último dógito
    dr = num_romano[i]
    dr_seguinte = num_romano[i+1]
    if valores_romanos[dr] >= valores_romanos[dr_seguinte]:
        decimal += valores_romanos[dr]
    else:
        decimal -= valores_romanos[dr]
decimal += valores_romanos[num_romano[-1]]  # Tratamento do último dígito

print(decimal)
