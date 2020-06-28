import sys

sys.stdin = open('색칠하기.txt', 'r')


# (1) 레드와 블루의 2차원 리스트를 생성한다. (10x10)
# (2) 리스트를 0으로 생성하고 색이 칠해져있으면 +1로 한다
# (3) 색이 3개이상이다.
T = int(input())
for t in range(T) :
    color_num = int(input()) ### 색칠하는 횟수
    matrix_ = []
    for jj in range(10):
        row_ = [0] * 10
        matrix_.append(row_)


    for i in range(color_num): ## 어디 칠하고 무슨색 칠할 껀지
        color_info = input().split()
        color_info = list(map(int,color_info))
        ## 빨간색은 1로 설정하고 파란색 2로 설정해서 보라색이면 3이 나오겠지 3인 점만 찾으면 됨
        for j in range(color_info[0], color_info[2]+1) :
            for k in range(color_info[1], color_info[3]+1) :
                matrix_[j][k] += color_info[4]

    purple = 0
    for a in range(10) :
        for b in range(10) :
            if matrix_[a][b] == 3 :
                purple += 1
            else :
                pass



    print(f'#{t+1} {purple}')



