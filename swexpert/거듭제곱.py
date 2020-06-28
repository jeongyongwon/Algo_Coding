import sys
sys.stdin = open('거듭제곱.txt', 'r')


T = 10
for t in range(T) :
    c = int(input())
    a, b = map(int, input().split())
    print(f'#{t+1} {a**b}')