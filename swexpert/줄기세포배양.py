import sys
sys.stdin = open('줄기세포배양.txt','r')

for t in range(1,int(input())+1):

    ### 센터 포인트에 박아야됨 !!!!!
    ### 센터에 박으려면 ...
    ### 세로와 가로의 절반에 반올림 한 구간에


    ### 생명력은 1~10  / 0은 생명력이 존재 하지 않음
    ## 생명력 수치가 X인 줄기세포는
    #  초기상태로부터 X시간동안은 비활성  -> 그 이후는 x 시간 동안 살아남을 수 있다
    ## 죽은 상태로 해당 그리드 셀을 차지하게 된다
    ## 죽더라도 X 라는 시간은 살아 남아있고
    ### 상하좌우로 번식하고 만약에 번식구역에 있는 생명력이 더 크면 번식 x
    ###  세로 크기, 가로 크기, 배양 시간

    N, M, K = map(int,input().split())



    #
    # ### 체킹 할 포인트
    # start_r = int((N+K)/N)
    # start_c = int((M+K)/M)
    _mat = [] ## 쑤셔 넣을 것
    for i in range(N):
        _mat.append(list(map(int,input().split())))


    for i in range(len(_mat)):
        for j in range(K):
            _mat[i].append(0)

    for i in range(len(_mat)):
        _mat[i][0:0] = [0] * K

    mat = [[0] * (len(_mat[0])) for _ in range(2*K) ]  ## 쑤셔 놓을 곳

    mat[int(len(mat)/2) :0 ] = _mat


    time = [ [-2] * len(mat[0])  for _ in range(len(mat)) ]


    turn = -1
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    res = 0
    ## 활성화 시키는 행렬을 만든다
    ## 만약 조회 후 지금 turn의 값이 동일할 때 활성화시키고 X의 시간이 2배일 때  활동 하는 것을 멈춘다
    ## 배양 시간이 K에 도달 했을 때 끝나면 됨
    ## 번식은 초기상태에서 X+1 에 번식함

    while turn < K :

        turn += 1

        ### 활성시간 변경
        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if time[i][j] == -2 :
                    time[i][j] = 0
                if mat[i][j] > 0 and time[i][j] != -1:
                    time[i][j] += 1


        ## 죽어버린 상태는 -1 로 표현하기
        ### 만약 time 값이 같다면 활성화로 만듬
        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if mat[i][j] + 1 == time[i][j] and time[i][j] != -1 and time[i][j] != 0 : ## 세포가 죽은 상태가 아니어야 함
                    time[i][j] = -1
                    for k in range(4):
                        r_ = i + dy[k]
                        c_ = j + dx[k]

                        if 0 <= r_ < N+(2*K) and 0 <= c_ < M+(2*K) and  time[r_][c_] == 0 and mat[r_][c_] == 0  :  ### 이 경우는 빈칸인 거에 처리를 해주는 것이다
                            if  mat[r_][c_] < mat[i][j]  :
                                mat[r_][c_] = mat[i][j]
                                time[r_][c_] = 0

                        elif 0 <= r_ < N + (2 * K) and 0 <= c_ < M + (2 * K) and time[r_][c_] == 0 and mat[r_][c_] < mat[i][j] :  ### 이 경우는 빈칸인 거에 처리를 해주는 것이다
                            if mat[r_][c_] < mat[i][j]:
                                mat[r_][c_] = mat[i][j]
                                time[r_][c_] = 0

                        ### 둘 다 활성상태일 때는 침범 x  -> 둘다 활성 상태인 것을 어찌 찾냐








    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] > 0 and time[i][j] >= 0 :
                res += 1


    print(f'#{t} {res}')


