

def dfs(r,c,cnt):
    global L
    global visited
    global mat
    if visited[r][c] :
        return
    if cnt == L :
        return

    visited[r][c] = 1

    #상하좌우
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    ## 원통에 따라 좌표 다르게

    if mat[r][c] == 1:
        for i in range(4):
            r_ = r + dy[i]
            c_ = c + dx[i]
            if 0 <= r_ < R and 0 <= c_ < C:
                if i == 0:

                    if mat[r_][c_] == 1 or mat[r_][c_] == 2 or mat[r_][c_] == 5 or mat[r_][c_] == 6:
                        dfs(r_, c_, cnt + 1)

                elif i == 1 :
                    if mat[r_][c_] == 1 or mat[r_][c_] == 2 or mat[r_][c_] == 4 or mat[r_][c_] == 7 :
                        dfs(r_,c_,cnt+1)

                elif i == 2 :
                    if mat[r_][c_] == 1 or  mat[r_][c_] == 3 or mat[r_][c_] == 4 or  mat[r_][c_] == 5:
                        dfs(r_,c_,cnt+1)
                else:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 3 or  mat[r_][c_] == 6 or mat[r_][c_] == 7:
                        dfs(r_,c_,cnt+1)

    if mat[r][c] == 2:
        for i in range(4):
            r_ = r + dy[i]
            c_ = c + dx[i]
            if 0 <= r_ < R and 0 <= c_ < C:
                if i == 0:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 2 or mat[r_][c_] == 5 or mat[r_][c_] == 6:
                        dfs(r_, c_, cnt + 1)

                if i == 1:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 2 or mat[r_][c_] == 4 or mat[r_][c_] == 7:
                        dfs(r_, c_, cnt + 1)


    if mat[r][c] == 3:
        for i in range(4):
            r_ = r + dy[i]
            c_ = c + dx[i]
            if 0 <= r_ < R and 0 <= c_ < C:
                if i == 2:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 3 or mat[r_][c_] == 4 or mat[r_][c_] == 5:
                        dfs(r_, c_, cnt + 1)

                if i == 3:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 3 or mat[r_][c_] == 6 or mat[r_][c_] == 7:
                        dfs(r_, c_, cnt + 1)



    if mat[r][c] == 4:
        for i in range(4):
            r_ = r + dy[i]
            c_ = c + dx[i]
            if 0 <= r_ < R and 0 <= c_ < C:
                if i == 0:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 2 or mat[r_][c_] == 5 or mat[r_][c_] == 6:
                        dfs(r_, c_, cnt + 1)

                if i == 3:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 3 or mat[r_][c_] == 6 or mat[r_][c_] == 7:
                        dfs(r_, c_, cnt + 1)


    if mat[r][c] == 5:
        for i in range(4):
            r_ = r + dy[i]
            c_ = c + dx[i]
            if 0 <= r_ < R and 0 <= c_ < C:
                if i == 1:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 2 or mat[r_][c_] == 4 or mat[r_][c_] == 7:
                        dfs(r_, c_, cnt + 1)

                if i == 3:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 3 or mat[r_][c_] == 6 or mat[r_][c_] == 7:
                        dfs(r_, c_, cnt + 1)


    if mat[r][c] == 6:
        for i in range(4):
            r_ = r + dy[i]
            c_ = c + dx[i]
            if 0 <= r_ < R and 0 <= c_ < C:
                if i == 1:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 2 or mat[r_][c_] == 4 or mat[r_][c_] == 7:
                        dfs(r_, c_, cnt + 1)
                if i == 2:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 3 or mat[r_][c_] == 4 or mat[r_][c_] == 5:
                        dfs(r_, c_, cnt + 1)



    if mat[r][c] == 7:
        for i in range(4):
            r_ = r + dy[i]
            c_ = c + dx[i]
            if 0 <= r_ < R and 0 <= c_ < C:
                if i == 0:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 2 or mat[r_][c_] == 5 or mat[r_][c_] == 6:
                        dfs(r_, c_, cnt + 1)
                if i == 2:
                    if mat[r_][c_] == 1 or mat[r_][c_] == 3 or mat[r_][c_] == 4 or mat[r_][c_] == 5:
                        dfs(r_, c_, cnt + 1)




import sys
sys.stdin = open("탈주범검거.txt",'r')

for t in range(1,int(input())+1):
    R,C,R_pot,C_pot,L = map(int,input().split())

    mat = []
    for r in range(R):
        mat.append(list(map(int,input().split())))

    visited = [[0] * C for _ in range(R)]

    dfs(R_pot,C_pot,0)

    result = 0
    for i in range(len(visited)):
        result += sum(visited[i])

    print(f'#{t} {result}')
    for i in range(len(visited)):
        print(visited[i])

