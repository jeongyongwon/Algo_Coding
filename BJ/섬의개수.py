import sys
sys.stdin = open('섬의개수.txt','r')



def search(r,c):
    global visited
    global cnt
    global mat
    global dy
    global dx
    global w
    global h

    if visited[r][c]:
        return

    visited[r][c] = 1


    for i in range(len(dy)):
        r_ = r + dy[i]
        c_ = c + dx[i]
        if 0 <= r_ < h and 0 <= c_ < w and visited[r_][c_] == 0 and mat[r_][c_] == 1:
            search(r_,c_)



for i in range(6):
    w, h = map(int,input().split())

    mat = []

    for i in range(h):
        mat.append(list(map(int,input().split())))

    visited = [[0] * w for _ in range(h)]


    cnt = 0
    ## 상 하 좌 우 , 상좌, 상우, 하좌 , 하우
    dy = [-1,1,0,0,-1,-1,1,1]
    dx = [0,0,-1,1,-1,1,-1,1]

    for i in range(h):
        for j in range(w):
            if mat[i][j] == 1 and visited[i][j] == 0 :
                search(i,j)
                cnt += 1


    print(cnt)
