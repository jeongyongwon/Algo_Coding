import sys
sys.stdin = open('재관이의대량할인.txt','r')

for t in range(1,int(input())+1):
    N = int(input())
    wear = list(map(int,input().split()))
    wear.sort(reverse=True)

    price = 0
    wear_len = len(wear)


    if wear_len % 3 == 0:
        for i in range(0, wear_len,3 ):
            price += wear[i] + wear[i+1]

    elif wear_len % 3 == 1:
        for i in range(0, wear_len,3 ):
            if i == wear_len -1 :
                price += wear[i]
            else :
                price += wear[i] + wear[i+1]


    else :
        for i in range(0, wear_len,3 ):
            if i == wear_len -1 :
                price += wear[i] + wear[i+1]
            else :
                price += wear[i] + wear[i+1]

    print(f'#{t} {price}')