def dfs(r,c):
    global is_found
    if visited[r][c] :
        return
    visited[r][c] = 1

    ## 상하좌우 설정
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]


    ### 주위에 좌표중 0인 것을 찾음
    for k in  range(len(dy)):
        r_ = r + dy[k]
        c_ = c + dx[k]
        if 0 <= r_ < 16 and 0 <= c_ < 16:
            if visited[r_][c_] == 0 and mat[r_][c_] == 0   :
                dfs(r_,c_)
            elif mat[r_][c_] == 3:
                is_found = 1

import sys
sys.stdin = open('미로1.txt','r')

t = 10
for tt in range(t):
    t_num = int(input())
    mat = []
    for i in range(16):
        mat.append( list( map(int,list(input()) )))

    now_r, now_c = 1, 1
    goal_r, goal_c = 13, 13
    is_found = 0


    visited = [[0] * 16 for _ in range(16)]
    dfs(now_r,now_c)

    if is_found == 1 :
        print('#{} 1'.format(tt+1))
    else :
        print('#{} 0'.format(tt+1))
