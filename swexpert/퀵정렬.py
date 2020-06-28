import sys
sys.stdin = open('병합정렬.txt','r')

for t in range(1,int(input())+1):
    N = int(input())
    num = sorted(list(map(int, input().split())))
    print(f'#{t} {num[N//2]}')