import sys
sys.stdin = open('염라대왕의이름정렬.txt','r')


for t in range(1,int(input())+1):
    N = int(input())
    name_list = []

    for i in range(N):
        name_list.append(input())

    name_list = list(set(name_list))
    name_list.sort()
    print(name_list)
    name_list = sorted(name_list,key=len)

    print(f'#{t}')
    for i in range(len(name_list)):
        print(name_list[i])