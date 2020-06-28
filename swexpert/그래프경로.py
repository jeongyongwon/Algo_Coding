def DFS(n) :
    if visit[n] :
        return
    visit[n] = 1
    for i in range(1,v+1):
        if visit[i] == 0 and mat[n][i] :
            DFS(i)






import sys
sys.stdin = open('그래프경로.txt', 'r')


t = int(input())
for tt in range(t):
    v, e = map(int,input().split())
    mat = [[0]*(v+1) for _ in range(v+1)]

    for i in range(e):
        s, g = map(int,input().split())
        mat[s][g] = 1

    start, goal = map(int,input().split())


    for kk in range(len(mat)):
        print(mat[kk])


    visit = [0 for _ in range(v+1)]




    DFS(start)
    if visit[goal] :
        print("#{} 1".format(tt+1))
    else:
        print("#{} 0".format(tt+1))
