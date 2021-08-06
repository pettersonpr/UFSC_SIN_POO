gabarito_1 = input()
gabarito_2 = input()

num_acertos = 0

for i in range(len(gabarito_1)):
    if gabarito_1[i] == gabarito_2[i]:
        num_acertos += 1

print(num_acertos)
