import sys
sys.stdin = open('어디에 단어가 들어갈 수 있을까.txt', 'r')
T = int(input())
for t in range(T) :
    n, k = map(int,input().split())
    matrix_ = []
    for nn in range(n):
        matrix_.append(list(map(int,input().split())))
    ## 1이 흰색 0이 검은색
    ### 길이가 블록처럼 딱 맞아야함

    #가로 case 부터
    cnt = 0

    for i in range(n):
        for j in range(n-k+1):
            if sum(matrix_[i][j:j+k]) != k :
                pass
            else :
                if j == 0 :
                    if matrix_[i][j+k] == 0 :
                        cnt +=1
                    else :
                        pass
                elif j == n-k :
                    if matrix_[i][j-1] == 0 :
                        cnt += 1
                    else :
                        pass

                elif 0< j < n - k :
                    if matrix_[i][j-1] == 0 and  matrix_[i][j+k] == 0 :
                        cnt += 1
                    else :
                        pass

    ## 세로 case
    for a in range(n):  ## 열 넘버
        for b in range(n-k+1): ## 행 넘버 => 최대한 갈수 있는
            cal_ = 0

            for c in range(k):
                cal_ += matrix_[b+c][a]

            if cal_ != k :
                pass
            else :
                if  b == 0 :
                    if matrix_[b+k][a] == 0:
                        cnt += 1
                    else :
                        pass
                elif b == n-k :
                    if matrix_[b-1][a] == 0:
                        cnt += 1
                    else :
                        pass
                elif 0 < b < n-k :
                    if matrix_[b+k][a] == 0 and matrix_[b-1][a] == 0 :
                        cnt += 1
                    else :
                        pass


    print(f'#{t+1} {cnt}')

















