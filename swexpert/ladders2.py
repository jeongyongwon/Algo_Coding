import sys

sys.stdin = open('ladders2.txt', 'r')

T = int(input())
for t in range(T):
    mat = []
    for n in range(100):
        mat.append(list(map(int, input().split())))
    result_list = [ ]
    ###하,좌,우
    dy = [1,0,0]
    dx = [0,-1,1]





    for i in range(100) : ### i는 출발점 열 번호
        if matrix_[0][i] == 0 :
            pass
        else :
            is_end = True
            cnt = 0
            start_col = i  ### 특정 출발점에서 시작하는 case만 나오는 거임
            start_row = 0
            ## 핵심은 방향을 틀었을 때이다.
            ## 만약 방향을 틀었다면 그거를 확인할 수 지표가 필요하다

            while is_end :
                if start_row == 99 :
                    is_end = False
                else:
                    if start_col == 0 :  ## 맨 왼쪽 열일 경우 case
                        if matrix_[start_row][start_col+1] == 1 :
                            is_direct = True
                            while is_direct:
                                if matrix_[start_row][start_col + 1] == 0 :
                                    is_direct = False
                                else :
                                    start_col += 1
                                    cnt += 1 ### 오른쪽으로 빠져나가기
                        elif matrix_[start_row][start_col+1] == 0: ## 옆으로 빠져나갈 경우가 없을 때 밑으로만 직진하기
                            start_row = start_row + 1
                            cnt += 1
                    elif 0 < start_col < 99 : ## 두번째 줄부터 99번째 줄까지  # 여기가 핵심인듯 좌우로 와리가리 하는 거 잡아야할 듯
                        if matrix_[start_row][start_col+1] == 1 :
                            is_direct2 = True
                            while is_direct2:
                                if matrix_[start_row][start_col + 1] == 0:
                                    is_direct2 = False
                                else:
                                    start_col += 1
                                    cnt += 1
                        elif matrix_[start_row][start_col-1] == 1:
                            is_direct3 = True
                            while is_direct3:
                                if matrix_[start_row][start_col - 1] == 0:
                                    is_direct3 = False
                                else:
                                    start_col -= 1
                                    cnt += 1
                        elif matrix_[start_row][start_col-1] == 0 and matrix_[start_row][start_col+1] and 0 :
                            start_row = start_row + 1
                            cnt += 1


                    elif i == 99 :
                        if matrix_[start_row][start_col-1] == 1 :
                            is_direct2 = True
                            while is_direct4:
                                if matrix_[start_row][start_col + 1] == 0:
                                    is_direct4 = False
                                else:
                                    start_col += 1
                                    cnt += 1
                        elif matrix_[start_row][start_col-1] == 0 :
                            start_row = start_row + 1
                            cnt += 1

                    else :
                        pass



    print(cnt)













