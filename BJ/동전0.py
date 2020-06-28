n, money = map(int,input().split())
coin_list = []

for i in range(n):
    coin_list.append(int(input()))

coin_list = sorted(coin_list, reverse=True)
cnt = 0
i = 0
is_end = True
while is_end :
    coin = coin_list[i]

    if money // coin  == 0:
        i += 1

    else :
        cnt += money // coin
        money -= (money // coin ) * coin


        if money == 0 :
            is_end = False
            break

        else :
            i += 1

print(cnt)