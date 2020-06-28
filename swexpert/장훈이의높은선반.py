import sys
sys.stdin = open('장훈이의높은선반.txt', 'r')

import itertools

for t in range(1,int(input())+1):
    N,B = map(int,input().split())
    emp = list(map(int,input().split()))
    result = []
    for i in range(1,len(emp)+1):
        com_list = list(itertools.combinations(emp,i))
        for j in range(len(com_list)):
            if sum(com_list[j]) >= B:
                result.append(sum(com_list[j])-B)

    result.sort()
    print(f'#{t} {result[0]}')














