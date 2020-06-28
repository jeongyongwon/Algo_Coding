import sys


def dfs(n):
    if visited[n]:
        return
    visited[n] = 1
    for i in range(1, V + 1):
        if adj_mat[n][i] and visited[i] == 0:
            dfs(i)


sys.stdin = open("그래프경로.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj_mat = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        nodes = list(map(int, input().split()))
        adj_mat[nodes[0]][nodes[1]] = 1
    start, end = map(int, input().split())

    dfs(start)
    if visited[end]:
        print("#{} 1".format(test_case))
    else:
        print("#{} 0".format(test_case))