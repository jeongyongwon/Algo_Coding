N, M, V = map(int,input().split())


mat = [[] for _ in range(N+1) ]

for i in range(M):
    S, G = map(int,input().split())
    mat[S].append(G)
    mat[G].append(S)



dfs_visited = [0 for _ in range(N+1)]
bfs_visited = [0 for _ in range(N+1)]

dfs_list = []
bfs_list = []

def dfs(START):
    global dfs_visited
    global dfs_list
    global mat

    if dfs_visited[START]:
        return
    dfs_visited[START] = 1
    if START not in dfs_list:
        dfs_list.append(START)

    is_end = True
    i = 0
    start = 0
    mat[START].sort()

    while is_end :
        if i >= len(mat[START]):
            is_end = False
            break


        elif dfs_visited[mat[START][i]] == 0:
            start = mat[START][i]

            if start == 0:
                pass
            else:
                dfs(start)
        else :
            i += 1


dfs(V)


queue_list = [V]

while len(queue_list) != 0:
    Start = queue_list.pop(0)
    mat[Start].sort()
    if Start not in bfs_list:
        bfs_list.append(Start)
        bfs_visited[Start] += 1

    for i in range(len(mat[Start])):
        if bfs_visited[mat[Start][i]] == 0 :
            queue_list.append(mat[Start][i])


print(' '.join(list(map(str,dfs_list))))
print(' '.join(list(map(str,bfs_list))))
