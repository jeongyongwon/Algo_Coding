def dfs(r,c,real):

    if len(real) == 7 :
        if real not in result :
            result.append(real)
        return

    dy = [-1,1.0,0]
    dx = [0,0,-1,1]
    for s in range(len(dy)):
        r_ = int(r+dy[s])
        c_ = int(c+dx[s])
        if 0<= r_ < 4 and 0<= c_ <4:
            dfs(r_,c_,real+str(mat[r_][c_]))

import sys
sys.stdin = open('격자판의숫자이어붙이기.txt', 'r')
for t in range(1,int(input()) + 1) :
    mat = []
    for ii in range(4):
        mat.append(list(map(int,input().split())))

    result = []
    for i in range(4):
        for j in range(4):
            dfs(i,j,str(mat[i][j]))


    print(f'#{t} {len(result)}')