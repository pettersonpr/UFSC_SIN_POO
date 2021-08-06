frase = input().lower().replace(' ','')

maior_ocorrencia = -1
letra_mais_ocorre = ' '

for letra in set(frase):
    ocorrencias = frase.count(letra)
    if ocorrencias > maior_ocorrencia:
        maior_ocorrencia = ocorrencias
        letra_mais_ocorre = letra

print(letra_mais_ocorre)
