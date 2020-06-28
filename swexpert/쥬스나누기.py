import sys
sys.stdin = open('쥬스나누기.txt', 'r')

T = int(input())
for t in range(T):
    n = int(input())
    result = (f'1/{n}' + ' ') * n

    print (f'#{t+1} {(result)}'  )

