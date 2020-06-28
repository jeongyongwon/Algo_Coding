price = 1000 - int(input())


ann = [500,100,50,10,5,1]

cnt = 0

for i in ann:
    if price == 0:
        pass
    else :
        a = price // i
        if a == 0 :
            pass
        else :
            price -= a * i
            cnt += a

print(cnt)



