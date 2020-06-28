import sys
sys.stdin = open('회문2.txt' ,'r')


for t in range(10):
    t_num = int(input())
    mat = []
    for nn in range(100) :
        ak = list(input())
        mat.append(ak)

    leng1 = 0

    # 가로부터 검증  / 홀수랑 짝수랑 case가 나눠져 있음
    ## 짝수 case
    for i in range(100):
        for j in range(99):
            if mat[i][j] == mat[i][j+1] :
                p = 0
                is_end = True
                while is_end :
                    if j-p <= -1 or j+1+p >= 100 :
                        is_end = False

                    elif mat[i][j-p] != mat[i][j+1+p] :
                        is_end = False

                    elif mat[i][j-p] == mat[i][j+1+p] :
                        p += 1
                if 2 * p > leng1:
                    leng1 = 2 * p
                else:
                    pass


            else :
                pass


    ## 홀수 case

    for i in range(100) :
        for j in range(99) :
            p = 1
            is_end = True
            while is_end :
                if j-p <= -1 or j+p >= 100 :
                    is_end = False
                elif mat[i][j-p] != mat[i][j+p] :
                    is_end = False
                elif mat[i][j-p] == mat[i][j+p] :
                    p+= 1
            if 2*p - 1 > leng1:
                leng1 = 2*p - 1





    ## 세로 검증
    ## 세로 배열을 가로로 만든 다음 검증하는 과정을 거치자
    #홀수랑 짝수랑 case가 나눠져 있음

    leng2 = 0
    rmat = []
    for j in range(100):
        test = []
        for i in range(100):
            test.append(mat[i][j])

        rmat.append(test)

    for i in range(100):
        for j in range(99):
            if rmat[i][j] == rmat[i][j+1] :
                p = 0
                is_end = True
                while is_end :
                    if j-p <= -1 or j+1+p >= 100 :
                        is_end = False

                    elif rmat[i][j-p] != rmat[i][j+1+p] :
                        is_end = False

                    elif rmat[i][j-p] == rmat[i][j+1+p] :
                        p += 1
                if 2 * p > leng2:
                    leng2 = 2 * p
                else:
                    pass


            else :
                pass

    for i in range(100):
        for j in range(99):
            p = 1
            is_end = True
            while is_end:
                if j - p <= -1 or j + p >= 100:
                    is_end = False
                elif rmat[i][j - p] != rmat[i][j + p]:
                    is_end = False
                elif rmat[i][j - p] == rmat[i][j + p]:
                    p += 1
            if 2 * p - 1 > leng2:
                leng2 = 2 * p - 1


    result = 0
    if leng1 > leng2 :
        result = leng1
    else :
        result = leng2

    print(f'#{t+1} {result}')























