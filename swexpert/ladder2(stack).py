def dfs(r,c):
    if visited[r][c]:
        return
    visited[r][c] = 1
    
    
    ## 하좌우
    dy = [1,0,0]
    dx = [0,-1,1]
    ### 좌우바꾸는거 생각해야함
    for k in range(len(dy)):
        r_ = r + dy[k]
        c_ = c + dx[k]
        if mat[r_][c_] == 1 :
            dfs(r_,c_)
            






import sys
sys.stdin = open('ladders2.txt', 'r')

T = int(input())
for t in range(T):
    mat = []
    for n in range(100):
        mat.append(list(map(int, input().split())))



    visited = [[0]*100  for _ in range(100) ]
    

