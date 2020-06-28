

def dfs(r):
    global res
    global result
    if r == N :
        return
    for i in range(N):

        if check[r][i] > 0 :
            continue

        res +=  mat[r][i]
        mark(r,i)

        dfs(r+1)
        if r == N-1:
            result.append(res)

        res -= mat[r][i]
        unmark(r,i)



def mark(r,c):
    # 가로줄 부터 다 마킹
    for i in range(N):
        check[r][i] += 1
    # 세로줄 부터 다 마킹
    for i in range(N):
        check[i][c] += 1


def unmark(r, c):
    # 가로줄 부터 다 마킹
    for i in range(N):
        check[r][i] -= 1
    # 세로줄 부터 다 마킹
    for i in range(N):
        check[i][c] -= 1


import sys
sys.stdin = open('배열최소합.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    mat = []

    for i in range(N):
        mat.append(list(map(int,input().split())))



    check = [[0] * N for _ in range(N)]
    res = 0
    result = []

    dfs(0)
    print(f'#{t+1} {min(result)}')