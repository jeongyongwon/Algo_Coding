import sys
sys.stdin = open('수의 새로운 연산.txt', 'r')


T = int(input())
for t in range(T) :
    so1, so2 = map(int,input().split())
    matrix_  = []
    for k in range(301):
          matrix_.append([0 * 301] * 301)


    dif = 1

    ### i가 y좌표 j가 x좌표
    for i in range(300) :
        start_ =  1 + int(i * (i+1)/2)
        dif = dif + 1
        for j in range(300):
            matrix_[i+1][j+1] =  int(start_ +   int(j)* (2*dif -1 + j)/ 2 )


    x1,x2,y1,y2 = 0,0,0,0

    # so1부터 검증
    for a in range(len(matrix_)):
        for b in range(len(matrix_)) :
            if matrix_[a][b] == so1 :
                x1 =  b ; y1 =  a

            if  matrix_[a][b] == so2 :
                x2 = b;
                y2 = a





    print(f'#{t+1} {matrix_[y1+y2][x1+x2]}')








