import sys
sys.stdin = open('미로.txt', 'r')

def dfs(r,c):
    if vis[r][c] :
        return
    vis[r][c] += 1
    # 상하좌우
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    for k in range(len(dy)):
        r_ = r + dy[k]
        c_ = c + dx[k]
        if 0 <= r_ < N and 0 <= c_ < N :
            if mat[r_][c_] == 1 :
                pass
            else :
                 dfs(r_, c_)


T = int(input())
for t in range(T):
    N = int(input())
    mat = []
    for i in range(N):
        mat.append(  list(map(int,list(  input() ))))

    start_r = 0
    start_c = 0

    goal_r = 0
    goal_c = 0

    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2 :
                start_r = i
                start_c = j
            elif mat[i][j] == 3:
                goal_r = i
                goal_c = j



    vis = [[0] * N for _ in range(N)]



    dfs(start_r,start_c)

    if vis[goal_r][goal_c] == 1 :
        print(f'#{t+1} 1')
    else :
        print(f'#{t+1} 0')

    # for i in range(len(vis)):
    #     print(vis[i])
    #
    # print('--------------')