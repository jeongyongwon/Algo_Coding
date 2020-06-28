import sys
sys.stdin = open('회문0.txt', 'r')

T = int(input())
for t in range(T) :
    N, M = map(int,input().split())
    mat = []
    for i in range(N):
        mat.append(list(input()))

    result = []

    ## 가로부터 회문 검사
    for i in range(N) :
        for j in range(N-M+1):
            if mat[i][j:j+M] == list(reversed(mat[i][j:j+M])) :
                result.append(mat[i][j:j+M])
            else :
                pass

    ## 세로 회문 검사


    for j in range(N) : ## 열 넘버
        for i in range(N-M+1): ## 시작하는 행 넘버
            test = []
            for k in range(M):
                 test.append(mat[i+k][j] )
            if test == list(reversed(test)):
                result.append(test)
            else :
                pass


    print(f'#{t+1} ' + ''.join(result[0]) )