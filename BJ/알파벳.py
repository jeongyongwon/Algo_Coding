def search(r,c,cnt):
    global check, mat, dst, dy, dx, visited

    if alpha[mat[r][c]] == False :
        alpha[mat[r][c]] = True
        for i in range(len(dy)):
            r_ = r + dy[i]
            c_ = c + dx[i]
            if 0 <= r_ < R and 0 <= c_ < C and alpha[mat[r_][c_]] == False and visited[r_][c_] == 0 :
                visited[r_][c_] = 1
                search(r_,c_,cnt+1)
                alpha[mat[r_][c_]] = False
                visited[r_][c_] = 0
            else:
                if cnt > dst:
                    dst = cnt

dy = [-1,1,0,0]
dx = [0,0,-1,1]

R, C = map(int,input().split())

mat = []


for i in range(R):
    mat.append(list(input()))

visited = [[0] * C for _ in range(R)]

dst = 0

#### 알파벳이 현재 들어가있는지 체크 dictㅁ
alpha = {'A':False,'B':False,'C':False,'D':False,'E':False,'F':False,'G':False,'H':False,'I':False,'J':False,'K':False,'L':False
    ,'M':False,'N':False,'O':False,'P':False,'Q':False,'R':False ,'S':False,'T':False,'U':False,'V':False,'W':False,'X':False,'Y':False,'Z':False}

visited[0][0] = 1

search(0,0,1)
print(dst)
