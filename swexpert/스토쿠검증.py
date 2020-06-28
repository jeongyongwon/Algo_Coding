import sys
sys.stdin = open('스토쿠검증.txt','r')

t = int(input())
for tt in range(t):

    mat = []
    for  i in range(9):
        mat.append(list(map(int,input().split())))

    ### 검증해야할 것 가로 길이 합이 45
    ### 세로 길이 합도 45
    ### 3x3 행렬씩 걸러내기

    cnt = 0

    ## 가로
    for  i in range(len(mat)):
        if sum(mat[i]) != 45 :
            cnt += 1


    ## 세로
    for i in range(len(mat[0])): ## 세로
        test = 0
        for j in range(len(mat)):
            test += mat[j][i]
        if test != 45 :
            cnt += 1

    ### 3x3 씩 검증

    for i in range(0,9,3):
        for j in range(0,9,3):
            test = 0
            test += sum(mat[j][i:i+3])+sum(mat[j+1][i:i+3]) + sum(mat[j+2][i:i+3])
            if test != 45 :
                cnt += 1


    if cnt == 0 :
        cnt = 1
    else:
        cnt =0




    print(f'#{tt+1}',cnt)


