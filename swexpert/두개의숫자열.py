import sys
sys.stdin = open('두개의숫자열.txt', 'r')


T = int(input())
for t in range(T):
    n, m = map(int,input().split())
    a_list = list(map(int,input().split()))
    b_list = list(map(int,input().split()))

    leng = 0

    if len(a_list) > len(b_list) :
        leng = len(b_list)
        max_ = 0
        for i in range(len(a_list) - leng + 1) :
            cal_ = 0
            for j in range(leng) :
                cal_ += a_list[i+j] * b_list[j]
            if cal_ > max_ :
                max_ = cal_
            else :
                pass


    else :
        leng = len(a_list)
        max_ = 0
        for i in range(len(b_list) - leng + 1):
            cal_ = 0
            for j in range(leng):
                cal_ += b_list[i + j] * a_list[j]
            if cal_ > max_:
                max_ = cal_
            else:
                pass




    print(f'#{t+1} {max_}')



