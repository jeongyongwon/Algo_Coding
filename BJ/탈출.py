import sys
sys.stdin = open('탈출.txt','r')
for t in range(int(input())):
    R,C = map(int,input().split())

    mat = []
    for i in range(R):
        mat.append(list(input()))

    ## 방문 처리하기
    visited = [[0] * C for _ in range(R)]
    ## 물 턴 확인
    water  = [[0] * C for _ in range(R)]


    ### D는 굴
    ### S는 고슴도치 위치
    ### .은 빈 곳
    ### *은 물 차있는 곳
    ## 고슴도치는 상하좌우로 이동 가능
    ### X는 돌 통과 X
    #### 물을 찰 때 가능 여러가지 경로들을 시뮬이레이션

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    cave = []
    queue = []

    ### 동굴 위치 미리 파악
    ## 나중에 검증을 위해
    for i in range(R):
        for j in range(C):
           if mat[i][j] == 'D':
               cave = [i,j]
           if mat[i][j] == 'S':
               queue = [[i,j]]

    visited[queue[0][0]][queue[0][1]] = 1
    ## BFS 리스트

    water_turn = 0
    is_end = True
    while is_end :
        ### 물이 차는 한 턴
        #### while 문이 끝날 수 있는 경우
        ## 고슴도치가 D에 도착하던지 / 아예 못가던지  둘 중 하나이당
        ### 첫 번째는 방문여부로 판단하고 두 번째는 못가는 것을 판단

        water_turn += 1

        ### 우선 인접공간에 물을 가득차게 만들어서  미리 갈 곳을 정한다
        ### 첫 턴에 물만 딱 퍼지게 만들어야함
        for i in range(R):
            for j in range(C):
                if mat[i][j] == '*':
                    water[i][j] = water_turn


        for i in range(R):
            for j in range(C):
                if mat[i][j] == '*' and water[i][j] == water_turn :
                    for k in range(4):
                        r_ = i + dy[k]
                        c_ = j + dx[k]
                        if 0 <= r_ < R and 0 <= c_ < C and mat[r_][c_] == '.':
                            mat[r_][c_] = '*'

       ### 위에서 시작 좌표를 받아왔으므로 받아올 필요가 없다

        if len(queue) == 0 :
            is_end = False
            break

        is_end_2 = True
        #### 이미 사방향이 방문을 하였거나 물이 차있거나 돌이면 굳이 방문할 필요가 없으니까 굳이 방문할 필요가 없는 과정을 줄여줌
        while is_end_2:
            if len(queue) == 0 :
                is_end_2 = False
                break
            r, c = queue.pop(0)

            prove = 0

            for k in range(4):
                r_ = r + dy[k]
                c_ = c + dx[k]
                if 0 <= r_ < R and 0 <= c_ < C :
                    if mat[r_][c_] == '.' or mat[r_][c_] == 'D':
                        prove += 1

            if prove == 0 :
                pass
            else :
                is_end_2 = False
                break



        for k in range(4):
            r_ = r + dy[k]
            c_ = c + dx[k]

            if 0 <= r_ < R and 0 <= c_ < C and visited[r_][c_] == 0 and mat[r_][c_] != '*' and mat[r_][c_] != 'X':
                visited[r_][c_] = visited[r][c] + 1
                queue.append([r_,c_])


    if visited[cave[0]][cave[1]] == 0 :
        print('KAKTUS')
    else :
        print(visited[cave[0]][cave[1]]-1)


    # for i in range(R):
    #     print(mat[i])
    # print('---------')
    # for i in range(R):
    #     print(visited[i])
    # print('---------')
    # for i in range(R):
    #     print(water[i])
    #
    # print('111111111')



