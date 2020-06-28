import sys
sys.stdin = open('중간평균값구하기.txt','r')

for t in range(int(input())):
    num = list(map(int,input().split()))
    num.sort()
    del num[0]
    del num[-1]
    print(f'#{t+1} {round(sum(num)/len(num))}')