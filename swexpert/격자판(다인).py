import sys
sys.stdin = open('격자판의숫자이어붙이기.txt','r')

def dfs(r, c, num):
    if len(num) == 7:
        if num not in result:
            result.append(num)
        return

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for x in range(4):
        nr = r + dr[x]
        nc = c + dc[x]

        if 0 <= nr < len(arr) and 0 <= nc < len(arr):
            dfs(nr, nc, num+str(arr[nr][nc]))


T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = []

    for r in range(len(arr)):
        for c in range(len(arr)):
            dfs(r, c, str(arr[r][c]))


    print(result)
    print('#{} {}'.format(test_case, len(result)))