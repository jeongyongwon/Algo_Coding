def dfs(r,c):
    global N
    global percent
    global c_visited
    global result

    if  c_visited[c]:
        return

    c_visited[c] = 1
    test = mat[r][c]/100
   
    percent *= test
    if sum(c_visited) == N :
        if percent * 100 > result:
            result = percent * 100



    else :
        for i in range(N):
            if c_visited[i] == 1:
                pass
            else:
                dfs(r+1,i)
                c_visited[i] = 0







import sys
sys.stdin = open('동철이의일분배.txt', 'r')


for t in range(1,int(input())+1):
    N = int(input())
    mat = []
    for k in range(N):
        mat.append(list(map(int,input().split())))



    c_visited = [0 for _ in range(N)]
    percent = 1
    result = 1

    for k in range(N):
        dfs(0,k)
        c_visited[k] = 0


    print(result)

    # print(f'#{t}','%.6f'% per_result)










