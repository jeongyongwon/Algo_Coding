# def dfs(r,c):
#     global visited
#     global r_cnt
#     global c_cnt
#
#
#     if visited[r][c]:
#         return
#     visited[r][c] = 1
#
#     r_ = r + 1
#     if 0 <= r_ < n and 0 <= c < n and visited[r_][c] == 0 and mat[r_][c] == 1:
#         r_cnt += 1
#         dfs(r_, c)
#
#
#     c_ = c+1
#     if 0 <= r < n and 0 <= c_ < n and visited[r][c_] == 0 and mat[r][c_] == 1:
#         c_cnt += 1
#         dfs(r,c_)

def dfs_r(r,c):
    global visited
    global r_cnt



    if visited[r][c]:
        return
    visited[r][c] = 1

    r_ = r + 1
    if 0 <= r_ < n and 0 <= c < n and visited[r_][c] == 0 and mat[r_][c] == 1:
        r_cnt += 1
        dfs_r(r_, c)

def dfs_c(r,c):
    global visited
    global c_cnt



    if visited[r][c]:
        return
    visited[r][c] = 1

    c_ = c + 1
    if 0 <= r < n and 0 <= c_ < n and visited[r][c_] == 0 and mat[r][c_] == 1:
        c_cnt += 1
        dfs_c(r, c_)





import sys
sys.stdin = open('행렬찾기.txt', 'r')


for t in range(int(input())):
    n = int(input())
    mat = []
    for i in range(n):
        test = list(map(int,input().split()))
        mat.append(test)

    r_cnt = 1
    c_cnt = 1
    result_r = []
    result_c = []


    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0:
                mat[i][j] = 1

    visited = [[0] * n for _ in range(n)]

    mat_cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and mat[i][j] == 1:
                dfs_r(i,j)
                result_r.append(r_cnt)
                r_cnt= 1

            else:
                pass
 


    print(result_r)


