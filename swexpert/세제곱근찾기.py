import sys
import copy
sys.stdin = open('세제곱근.txt','r')


for t in range(int(input())):
    num = int(input())
    sosu = [2,3,5,7]
    res = [0,0,0,0]

    p = 0
    is_end = True
    while is_end :
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
            is_end = False

        if num % 2 == 0 :
            num = num / 2
            res[0] += 1


        if num % 3 == 0:
            num = num / 3
            res[1] += 1

        if num % 5 == 0:
            num = num / 5
            res[2] += 1

        if num % 7 == 0:
            num = num / 7
            res[3] += 1

    final_ = 1

    for i in range(len(res)):

        if res[i] % 3 == 1 or res[i] % 3 == 2:
            final_ = -1

        if res[i] % 3 == 0:
            final_ *= sosu[i] ** (res[i] // 3)

    print(f'#{t+1} {final_}')


## 1/3 승으로 하는 생각
## 시발 됫었네