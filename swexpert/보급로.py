# def dfs(r,c,cnt):
#     global visited, dy, dx, res, mat
#
#
#     if r == N-1 and c == N-1 :
#         if cnt < res :
#             res = cnt
#             return
#
#
#     for i in range(4):
#         r_ = r + dy[i]
#         c_ = c + dx[i]
#         if 0 <= r_ < N and 0 <= c_ < N :
#             if cnt+mat[r_][c_] < res:
#                 dfs(r_,c_,cnt+mat[r_][c_])
#

import sys
sys.stdin = open('보급로.txt','r')

for t in range(1,int(input())+1):
    N = int(input())

    mat = [ ]
    for i in range(N):
        arr = list(map(int,list(input())))
        mat.append(arr)

    # 0은 복구할 필요없다
    # 거리보단 복구 시간만 고려하면 된다


    res = float('inf')


    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    visited = [[0] * N for _ in range(N)]


    print(res)