import sys

sys.stdin = open('회문.txt', 'r')

for t in range(10):
    leng = int(input())

    mat = []
    for i in range(8):
        mat.append(list(input()))

    ## 가로 부터 검증하기
    cnt = 0
    for i in range(8):
        for j in range(8-leng+1):
            if mat[i][j:j+leng] == list(reversed(mat[i][j:j+leng])) :
                cnt += 1
            else :
                pass


    ## 세로 검증하기


    for j in range(8):
        for i in range(8-leng+1) :
            test = []
            for k in range(leng):
                test.append(mat[i+k][j])

            if test == list(reversed(test)) :
                cnt += 1
            else :
                pass


    print(f'{t+1} {cnt}')











