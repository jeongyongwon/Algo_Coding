

def virus(r,c):
    global mat, R, C

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    for i in range(4):
        r_ = r + dy[i]
        c_ = c + dx[i]
        if 0 <= r_ < R and 0 <= c_ < C and mat[r_][c_] == 0:
            mat[r_][c_] = 4
            virus(r_,c_)



def comb(idx,cnt,N,arr,selected):
    global wall_comb

    if cnt == N :
        comb_list = []
        for i in range(len(arr)):
            if selected[i]:
                comb_list.append(i)
        wall_comb.append(comb_list)
        return


    if idx == len(arr):
        return


    selected[idx] = 1
    comb(idx+1,cnt+1,N,arr,selected)
    selected[idx] = 0
    comb(idx+1,cnt, N, arr, selected)



### 2차원 배열 최대
cnt = 0
res = 0
R, C = map(int, input().split())
mat = []

for i in range(R):
    mat.append(list(map(int,input().split())))




### 벽을 세우는 모든 케이스 표시 해주기
# 벽은 무조건 3개만 새로 설치해주기
# 0은 안전구역
# 1은 벽 / 새로 설치한 벽은 3
# 2 바이러스 / 새로 퍼지는 바이러스는 4로 처리해주기

# 0인 곳에 벽을 세우는 케이스
# 뽑아준 좌표들을 3개씩 뽑는 조합식 만들기


wall_can = []

for i in range(R):
    for j in range(C):
        if mat[i][j] == 0:
            wall_can.append([i,j])

select = [0] * len(wall_can)
wall_comb = []
comb(0,0,3,wall_can,select)

res = 0
is_end = True

while is_end :

    if len(wall_comb) == 0 :
        is_end = False
        break


    else :
        wall = wall_comb.pop(0)

        ## 벽의 조합을 받고  그 좌표에 맞게 표시
        for i in wall:
            r, c = wall_can[i]
            mat[r][c] = 3


        ### 바이러스  퍼트림
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 2:
                    virus(i,j)


        cnt = 0

        ## 안전 구역 확인

        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0 :
                    cnt += 1

        ## 최대인지 검증

        if cnt > res :
            res = cnt

        ## 그리고 virus 제거 해야함

        for i in range(R):
            for j in range(C):
                if mat[i][j] == 4:
                    mat[i][j] = 0

        ## 벽도 제거

        for i in wall:
            r, c = wall_can[i]
            mat[r][c] = 0

print(res)