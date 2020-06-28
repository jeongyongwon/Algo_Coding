def prim_queue(G, r):
    global V, E
    INF = float("inf")
    weight = [INF] * (V+1)  # 가중치
    used = [False] * (V+1)  # 해당 정점이 이미 포함되었는가
    q = list()
    heapq.heappush(q, (0, r))
    result = 0
    while q:
        cw, cv = heapq.heappop(q)
        if used[cv]:
            continue
        used[cv] = True
        result += cw
        for u in range(V+1):
            if G[cv][u] > 0 and not used[u] and weight[u] > G[cv][u]:
                weight[u] = G[cv][u]
                heapq.heappush(q, (weight[u], u))

    return result

import sys, heapq
sys.stdin = open('최소신장트리.txt','r')

for t in range(1,int(input())+1):

    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]


    for i in range(E):  # 간선의 개수 만큼 반복
        s, e, c = map(int, input().split())
        adj[s][e] = c
        adj[e][s] = c

    result = prim_queue(adj, 0)
    print(f'#{t} {result}')

