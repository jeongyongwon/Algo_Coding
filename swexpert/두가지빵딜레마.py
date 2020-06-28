import sys
sys.stdin = open('두가지빵딜레마.txt','r')

for t in range(int(input())):
    a, b, c = map(int,input().split())
    ## only a case



    a_max = c//a
    i = a_max ## a
    j = 0 ## b
    can_max = c//a

    is_end = True
    while is_end :
        if c >= (i * a) + (b * j):
            if can_max < i + j :
                can_max = i + j
            else :
                pass
        else :
            pass
        if i == 0:
            is_end = False
        i -= 1 ; j += 1



    print(f'#{t+1} {can_max}')


