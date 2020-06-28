import sys
sys.stdin = open('달란트2.txt','r')

for t in range(1,int(input())+1):
    dallant, divide = map(int,input().split())

    result = 1
    if dallant % divide  == 0 :
        result = int(dallant / divide) ** divide

    else :
        res = int(dallant % divide)
        dallant -= res
        ls = [int(dallant/divide)] * divide

        is_end = True
        while is_end:
            if res == 0 :
                is_end = False
                break
            else :
                ls[ls.index(min(ls))] += 1
                res -= 1

        for i in ls:
            result *= i


    print(f'#{t} {result}')


