import sys
sys.stdin = open('두수의덧셈.txt','r')
for t in range(1,int(input())+1):
    a, b = map(int,input().split())
    print(f'#{t} {a+b}')
