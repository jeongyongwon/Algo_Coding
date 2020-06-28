import sys
sys.stdin = open('상호의배틀필드.txt', 'r')

T = int(input())
for t in range(T):
    h, w = map(int,input().split())

    mat = []
    for i in range(h):
        mat.append(list(input()))

    n = int(input())
    con = list(input())

    tank_direct = ['^','v','<','>']
    ## 상하좌우
    start_r = 0
    start_c = 0
    now_tank = ''

    for i in range(h):
        for j in range(w):
            if mat[i][j] in tank_direct:
                start_r = i
                start_c = j
                now_tank = mat[i][j]



    for cc in range(len(con)):

        if con[cc] == 'U':
            if start_r - 1 < 0 or mat[start_r-1][start_c] == '*' or mat[start_r-1][start_c] == '#' or mat[start_r-1][start_c] == '-' :
                mat[start_r][start_c] = '^' ## 앞으로 나아갈 수 없을 때는 그대로
            elif mat[start_r-1][start_c] == '.':
                mat[start_r][start_c] = '.'
                mat[start_r-1][start_c] = '^'
                start_r = start_r - 1




        if con[cc] == 'D':
            if start_r + 1 >= h or mat[start_r+1][start_c] == '*' or mat[start_r+1][start_c] == '#' or mat[start_r+1][start_c] == '-' :
                mat[start_r][start_c] = 'v'
            elif mat[start_r+1][start_c] == '.':
                mat[start_r][start_c] = '.'
                mat[start_r+1][start_c] = 'v'
                start_r = start_r + 1


        if con[cc] == 'L':
            if start_c - 1 < 0 or mat[start_r][start_c-1] == '*' or mat[start_r][start_c-1] == '#' or mat[start_r][start_c-1] == '-' :
                mat[start_r][start_c] = '<'
            elif mat[start_r][start_c-1] == '.':
                mat[start_r][start_c] = '.'
                mat[start_r][start_c - 1] = '<'
                start_c = start_c - 1


        if con[cc] == 'R':
            if start_c + 1 >= w or mat[start_r][start_c+1] == '*' or mat[start_r][start_c+1] == '#' or mat[start_r][start_c+1] == '-' :
                mat[start_r][start_c] = '>'
            elif mat[start_r][start_c+1] == '.':
                mat[start_r][start_c] = '.'
                mat[start_r][start_c+1] = '>'
                start_c = start_c + 1



        if con[cc] == 'S':
            if mat[start_r][start_c] == tank_direct[0]:  ##탱크방향 상
                i = 1
                is_up = True
                while is_up :
                    if start_r-i <= -1 : ### 게임 끝지점으로 쏘는거니까 종료
                        is_up = False
                    elif mat[start_r-i][start_c] == '*': ## 벽돌을 만나면 부수고 탄은 없어지고 평지로 변함
                        mat[start_r -i][start_c] = '.'
                        is_up = False
                    elif mat[start_r-i][start_c] == '#':
                        is_up = False
                    else :
                        i += 1



            if mat[start_r][start_c] == tank_direct[1]:  ##탱크방향 하
                j = 1
                is_down = True
                while is_down :
                    if start_r+j >= h :
                        is_down = False
                    elif mat[start_r+j][start_c] == '*':
                        mat[start_r+j][start_c] = '.'
                        is_down = False
                    elif mat[start_r+j][start_c] == '#':
                        is_down = False
                    else :
                        j += 1


            if mat[start_r][start_c] == tank_direct[2]:  ##탱크방향 좌
                k = 1
                is_left = True
                while is_left :
                    if start_c - k <= -1:
                        is_left = False
                    elif mat[start_r][start_c - k] == '*':
                        mat[start_r][start_c-k] = '.'
                        is_left = False
                    elif mat[start_r][start_c-k] == '#':
                        is_left = False
                    else :
                        k += 1

            if mat[start_r][start_c] == tank_direct[3]:  ##탱크방향 우
                l = 1
                is_right = True
                while is_right :
                    if start_c + l >= w :
                        is_right = False
                    elif mat[start_r][start_c+l] == '*':
                        mat[start_r][start_c+l] = '.'
                        is_right = False
                    elif mat[start_r][start_c+l] == '#':
                        is_right = False
                    else :
                        l += 1



    print(f'#{t+1}', end=' ')
    for item in mat:
        for j in range(len(item)):
            print(item[j], end='')
        print()