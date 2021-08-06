# Importar o módulo "math" (necessário para cálculo da raiz quadrada)
import math

# Obter os dados (valores de a, b, c)
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# Calcular delta
delta = b**2 - 4*a*c

# Calcular as raízes
if delta >= 0 and a != 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    # Imprimir o resultado
    print("As raízes reais são: ", x1, "e:", x2)
else:
    print("Não existe raiz")
