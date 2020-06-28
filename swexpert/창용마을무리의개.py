import sys
sys.stdin = open('창용마을무리의개수.txt','r')


for t in range(1,int(input())+1):
    N, M = map(int,input().split())

    connect = [[] for _ in range(N+1)]

    for i in range(M):
        start, end = map(int,input().split())
        connect[start].append(end)
        connect[end].append(start)


    visited = [ 0 for _ in range(N+1)]
    cnt = 0



    def dfs(r):
        global cnt
        global visited
        global connect

        for i in connect[r]:
            if  visited[i] == 0 :
                visited[i] = 1
                dfs(i)


    for i in range(1,len(connect)):
        if visited[i] == 0 :
            dfs(i)
            cnt += 1

    print(f'#{t} {cnt}')