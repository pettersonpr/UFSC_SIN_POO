#abcdefghijklmnopqrstuvwxyz
#PORTUGALBCDEFHIJKMNQSVWXYZ
#GSCPF QITIN TUJMUNNP! GIFIN TUNRIOUMQIN!

alfabeto_normal = input()
alfabeto_cifrado = input()
mensagem_cifrada = input()

mapeamento = dict(zip(alfabeto_cifrado, alfabeto_normal))
mensagem_normal = ''
for letra in mensagem_cifrada:
    if letra in mapeamento:
        mensagem_normal += mapeamento[letra]
    else:
        mensagem_normal += letra

print(mensagem_normal)

'''
mensagem_normal = ''
for letra in mensagem_cifrada:
    if letra in alfabeto_cifrado:
        ind = alfabeto_cifrado.index(letra)
        mensagem_normal += alfabeto_normal[ind]
    else:
        mensagem_normal += letra

print(mensagem_normal)
'''

