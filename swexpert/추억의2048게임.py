import sys

sys.stdin = open('추억의2048게임.txt', 'r')




T = int(input())
for t in range(T) :
    n,s = input().split()
    n = int(n)
    ## 판에 들어가는 숫자들은 2**n-1 임
    matrix_ = []
    for nn in range(n) :
        matrix_.append(list(map(int,input().split())))

    #### 상하좌우
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    ### 미는 방향의 제일 하위부터 시작
    ### else에 옵션넣어서 끌어오는거

    if s == 'up' :
        for i in range(n):
            for j in range(n-1):
                if matrix_[j][i] == 0:
                    matrix_[j][i] =  matrix_[j + 1][i]
                    matrix_[j + 1][i] = 0

                elif matrix_[j][i] ==  matrix_[j+1][i] :
                    matrix_[j][i] += matrix_[j + 1][i]
                    matrix_[j + 1][i] = 0

                else :
                    pass




    if s == 'down' :
        for a in range(n):
            for b in range(n-1):
                if matrix_[n-b-1][a] == 0:
                    matrix_[n-b-1][a] =  matrix_[n-b-2][a]
                    matrix_[n-b-2][a] = 0
                elif matrix_[n-b-1][a] ==  matrix_[n-b-2][a] :
                    matrix_[n-b-1][a] += matrix_[n-b-2][a]
                    matrix_[n-b-2][a] = 0
                else :
                    pass

    if s == 'right':
        for k in range(n) :
            for l in range(n-1):
                if matrix_[k][n-l-1] == 0 :
                    matrix_[k][n-l-1] = matrix_[k][n-l-2]
                    matrix_[k][n - l - 2] = 0
                elif matrix_[k][n-l-1] == matrix_[k][n-l-2] :
                    matrix_[k][n - l - 1] += matrix_[k][n - l - 2]
                    matrix_[k][n - l - 2] = 0
                else :
                    pass





    if s == 'left':
        for c in range(n):
            for d in range(n-1):
                if matrix_[c][d] == 0:
                    matrix_[c][d] = matrix_[c][d+1]
                    matrix_[c][d+1] = 0
                elif matrix_[c][d] == matrix_[c][d+1]:
                    matrix_[c][d] += matrix_[c][d+1]
                    matrix_[c][d+1] = 0
                else:
                    pass


    for pp in range(n) :
        print(matrix_[pp])


    print('-------------')

