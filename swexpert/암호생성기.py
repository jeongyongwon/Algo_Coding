import sys

sys.stdin = open('암호생성기.txt', 'r')

import collections


T = 10
a = 1
for t in range(T):
    t_num = int(input())
    list_ = list(map(int, input().split()))
    D = collections.deque(list_)



    i = 1
    is_end = True

    while is_end :
        D.append(D[0]-i)
        if D[len(D)-1] <= 0 :
            D[len(D) - 1] = 0
        D.popleft()
        i += 1
        if i == 6 :
            i = 1

        if D[len(D)-1] == 0:
            is_end = False


    result = list(D)
    result = list(map(str,result))


    print('#{0} '.format(t_num),' '.join(result)   )








