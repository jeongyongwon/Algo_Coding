def search(r,c):
    global cnt, checked, arr, mat, N, M

    if checked[r] :
        return

    if r != c :
        checked[r]= 1
    else :
        return

    for i in range(1,N+1):
        if checked[i] == 0 and mat[r][i] == 1 and r != i :
            search(i,r)


import sys
sys.stdin = open('그룹나누기.txt','r')


for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    # N은 몇명까지 M은 신청서
    arr = list(map(int,input().split()))

    ## 결과를 담기 위한 배열
    mat = [[0] * (N+1) for _ in range(N+1)]

    for i in range(0, len(arr) ,2):
        mat[arr[i]][arr[i+1]] = 1
        mat[arr[i+1]][arr[i]] = 1


    cnt = 0
    checked = [0]*(N+1)

    for i in range(1,N+1):
        for j in range(1,N+1):
            if i != j and checked[i] == 0 :
                search(i,j)
                cnt += 1


    print(f'#{t} {cnt}')