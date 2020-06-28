def recursion(l1, l2, arr):
    global cnt
    if sum(l1) not in arr:
        cnt += 1
        arr.update([sum(l1)])

    for i, x in enumerate(l2):
        recursion(l1 + [x], l2[i+1:],arr)


import sys
sys.stdin = open('가능한시험점수.txt','r')



for t in range(1,int(input())+1):
    pro_num = int(input())
    score = list(map(int,input().split()))
    result = set([])
    cnt = 0
    res = recursion([],score,result)
    print(f'#{t} {cnt}' )

