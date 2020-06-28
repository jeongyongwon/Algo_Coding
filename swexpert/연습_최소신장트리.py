import sys
sys.stdin = open('최소신장트리.txt','r')

for t in range(1,int(input())+1):
    V, E = map(int,input().split())
    mat = [[0] * (V+1) for _ in range(V+1)  ]

    for i in range(E):
        v1, v2, weight = map(int,input().split())
        mat[v1][v2] = weight
        mat[v2][v1] = weight


    # # key, p , mst 준비
    #
    # INF = float('inf')
    # key = [INF] * (V+1)
    # p = [-1] * (V+1) # 부모
    # mst = [False] * (V+1)
    #
    # #시작점 선택 : 0번 선택
    #
    # key[0] = 0
    # cnt = 0
    # result = 0
    # while cnt < V :
    #
    #     min = INF
    #     u = -1
    #     for i in range(V):
    #         if not mst[i] and key[i] < min :
    #             min = key[i]
    #             u = i
    #     ## u를 mst로 선택
    #     mst[u] = True
    #     result += min
    #     #key값을 갱신
    #     #u에 인접하고 아직 mst 아닌 정점 w에서 key[w] > u-w 가중치면 갱신
    #
    #     cnt += 1
    #
    #     for w in range(V+1):
    #         if mat[u][w] > 0 and not mst[w] and key[w] > mat[u][w] :
    #             key[w] = mat[u][w]
    #             p[w] = u # 부모
    #
    # print(key)
    # print(mst)
