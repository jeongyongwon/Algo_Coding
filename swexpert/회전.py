import sys
sys.stdin = open('회전.txt','r')


for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    list_ = list(map(int,input().split()))



    for i in range(M):
        first_item = list_[0]
        list_ = list_[1:]
        list_.append(first_item)


    print(f'#{t} {list_[0]}')



