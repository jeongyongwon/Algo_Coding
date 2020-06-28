import sys
sys.stdin = open('마그네틱.txt', 'r')

T = 10
for t in range(T):
    n = int(input())

    # 2차원 배열 생성
    mat = []
    for nn in range(n):
        mat.append(list(map(int, input().split() )))


    # 맨 끝에 있는 것들 중에 무조건 떨어지는 것들은 없애기
    for a in range(len(mat)) :
        if mat[0][a] == 2 :
            mat[0][a] = 0
        else :
            pass


        if mat[99][a] == 1:
            mat[99][a] = 0
        else :
            pass





    for i in range(len(mat)) :
        for j in range(0, len(mat)):
            if mat[j][i] == 2:
                cnt_1 = 0
                for k in range(0,j): # 2는 위로 가는 성질이니까 2 위에 1이 있는지 확인하는 과정
                    if mat[k][i] == 1:
                        cnt_1 +=1

                if cnt_1 == 0 :
                    mat[j][i] = 0
                else :
                    pass

            elif mat[j][i] == 1 :
                cnt_2 = 0
                for l in range(j+1, len(mat)): # 1은 아래로 가는 성질이니까 1 밑에 2가 하나라도 있는지 확인
                    if mat[l][i] == 2:
                        cnt_2 += 1
                if  cnt_2 == 0:
                    mat[j][i] = 0
                else :
                    if mat[j+1][i] == 0:
                        mat[j+1][i] = 1
                    elif mat[j+1][i] == 2:
                        pass

            else :
                pass

    cnt = 0
    for gg in range(len(mat)):
        for hh in range(len(mat)-1):
            if mat[hh][gg] == 1 and mat[hh+1][gg] == 2:
                cnt += 1
            else :
                pass


    print(f'#{t+1} {cnt}')

