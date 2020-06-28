import sys
sys.stdin = open('배열의분할.txt', 'r')


T = int(input())
for t in range(T):
    n = int(input())
    list_ = list(map(int,input().split()))

    cnt = 0


    if list_[0] < list_[1] : ## 오름차순 배열 걸러내는거
        k = 0
        is_end = True
        while is_end :

            if list_[k] <= list_[k+1]:
                k += 1
            else :
                k += 1
                cnt += 1
                is_end = False



    elif list_[k] > list_[i+1] :
        t = k
        is_end2 = True
        while is_end2 :

            if list_[t] >= list_[t+1] :
                t += 1
            else :
                t += 1
                cnt += 1
                is_end2 = False

    else :
