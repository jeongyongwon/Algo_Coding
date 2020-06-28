import sys
sys.stdin = open('미로의거리.txt','r')


for t in range(1,int(input())+1):
    N = int(input())
    mat = []
    for i in range(N):
        mat.append(list(map(int,input())))


    visited = [ [0] * N for _ in range(N) ]


    ## 상하좌우
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2 :

                visited[i][j] = 1
                is_end = True
                queue_list = [[i,j]]


                while len(queue_list) != 0 :

                    r,c = queue_list.pop(0)


                    for delta in range(len(dy)):
                        r_ = r + dy[delta]
                        c_ = c + dx[delta]

                        if 0 <= r_ <  N  and 0 <= c_ < N and visited[r_][c_] == 0 and mat[r_][c_] != 1 :
                            visited[r_][c_] = visited[r][c] + 1
                            queue_list.append([r_,c_])


            elif mat[i][j] == 3:
                goal_r, goal_c = i, j

            else :
                pass


    if visited[goal_r][goal_c] != 0 :
        print(f'#{t} {visited[goal_r][goal_c]-2}')
    else :
        print(f'#{t} {0}')

