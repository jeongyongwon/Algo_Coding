import sys
sys.stdin = open('홀짝일까.txt','r')

for t in range(int(input())):
    num = int(input())

    if num % 2 == 0 :
        print(f'#{t+1} Even')
    else :
        print(f'#{t + 1} Odd')