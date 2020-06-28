def dfs(r,c,end_r,end_c):
    global mat, cnt, res

    ## 우 하
    dy = [0,1]
    dx = [1,0]
    if r == end_r and c == end_c:
        if cnt < res:
            res = cnt


    for i in range(len(dy)):
        r_ = r + dy[i]
        c_ = c + dx[i]
        if 0 <= r_ < N and 0 <= c_ < N and mat[r_][c_] + cnt < res :
            cnt += mat[r_][c_]
            dfs(r_,c_,end_r,end_c)
            cnt -= mat[r_][c_]





import sys
sys.stdin = open('최소합.txt','r')

for t in range(1,int(input())+1):
    N = int(input())
    cnt = 0
    res = 1000
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))

    dfs(0,0,N-1,N-1)
    print(f'#{t} {res+mat[0][0]}')