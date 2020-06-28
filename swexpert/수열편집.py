import sys
sys.stdin = open('수열편집.txt','r')


for t in range(1,int(input())+1):
    N, M, L = map(int,input().split())
    num_list = list(map(int,input().split()))

    for i in range(M):
        DO = list(input().split())

        if DO[0] == 'I':
            num_list.insert(int(DO[1]),int(DO[2]))

        if DO[0] == 'D':
            del num_list[int(DO[1])]

        if DO[0] == 'C':
            num_list[int(DO[1])] = int(DO[2])


    if L >= len(num_list) or L < 0:
        print(f'#{t} -1')
    else :
        print(f'#{t} {num_list[L]}')