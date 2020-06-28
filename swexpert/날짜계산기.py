import sys
sys.stdin = open('날짜계산기.txt','r')

t = int(input())
for tt in range(t):
    final = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    m1, d1, m2, d2 = map(int,input().split())
    result = 0
    if m2 - m1 > 1:
        for i in range(1,m2-m1):
            result += final[m1+i]
        result += d2 + final[m1] - d1 +1

    elif m2 - m1 == 1 :
        result += d2  + final[m1] - d1 + 1

    else :
        result += d2 - d1 + 1

    print(f'#{tt+1} {result}')





