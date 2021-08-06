qtdd_pessoas = int(input())
qtdd_nome = 0

for i in range(qtdd_pessoas):
    nome = input()
    lista_nomes = nome.split()

    for n in lista_nomes:
        if n == 'Maria':
            qtdd_nome += 1

print(qtdd_nome)
