for _ in range(12):
    chuvas_mes = [int(w) for w in input().split()]
    media_mensal = sum(chuvas_mes)/len(chuvas_mes)
    print('{:.2f}'.format(media_mensal), end = ' ')
