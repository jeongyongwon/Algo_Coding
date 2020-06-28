
import sys
sys.stdin = open('정사각형방.txt','r')


for t in range(1,int(input())+1):
    N = int(input())
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))

    result_list = []
    visited = [[0] * N for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                r_ = i + dy[k]
                c_ = j + dx[k]
                if 0 <= r_ < N and 0 <= c_ < N and mat[r_][c_] == mat[i][j] + 1 :

                    cnt = 1
                    is_end = True
                    while is_end :

                        is_can = 0

                        for l in range(4):
                            r_deep =  r_ + dy[l]
                            c_deep =  c_ + dx[l]
                            if 0 <= r_deep < N and 0 <= c_deep < N and mat[r_deep][c_deep] == mat[r_][c_] + 1 :

                                r_ = r_deep
                                c_ = c_deep
                                cnt += 1
                                is_can += 1
                            else:
                                pass

                        if is_can == 0:
                            result_list.append([i,j, cnt ])
                            is_end = False

                else :
                    pass


    max_way = 0
    for a in range(len(result_list)):
        if result_list[a][2] > max_way :
            max_way = result_list[a][2]

    index_list = []
    for a in range(len(result_list)):
        if result_list[a][2] == max_way:
            index_list.append(mat[result_list[a][0]][result_list[a][1]])



    print(f'#{t} {min(index_list)} {max_way+1}')










