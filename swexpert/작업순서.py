


import sys
sys.stdin = open('작업순서.txt', 'r')


t = 10
for tt in range(t):
    v, e = map(int,input().split())
    list_ =  list(map(int,input().split()))

    mat = [[0] * (v+1) for _ in range(v+1) ]
    for i in range(0,len(list_),2):
        mat[list_[i]][list_[i+1]] = 1

        start_list = []

    for i in range(1,v+1):
        cnt = 0
        for j in range(1, v+1):
            if mat[j][i] == 1 :
                cnt = 1
            else :
                pass
        if cnt == 0 :
            start_list.append(i)


    visit = [[0] for _ in range(v+1)]

