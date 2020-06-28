import sys
sys.stdin = open('노드의거리.txt','r')


for t in range(1,int(input())+1):
    V, E = map(int,input().split()) # V 노드 , E 간선

    mat = [ [] for _ in range(V+1)  ]

    for i in range(E):
        start, goal= map(int,input().split())
        mat[start].append(goal)
        mat[goal].append(start)



    s,g = map(int,input().split())


    visited = [ 0 for _ in range(V+1)]
    visited[s] = 1

    queue_list = [s]
    while len(queue_list) != 0 :
        start = queue_list.pop(0)

        for i in mat[start] :
            if visited[i] == 0 :
                queue_list.append(i)
                visited[i] = visited[start] + 1


    if visited[g] != 0 :
        print(f'#{t} {visited[g]-1}')
    else :
        print(f'#{t} {0}')