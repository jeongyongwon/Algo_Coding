import sys
sys.stdin = open('숫자추가.txt','r')



for t in range(1,int(input())+1):
    N, M, L = map(int,input().split())
    num_list = list(map(int,input().split()))

    for i in range(M):
        index, num = map(int,input().split())
        num_list.insert(index,num)

    print(f'#{t} {num_list[L]}')