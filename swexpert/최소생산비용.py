def go(r,c,pay):
    global mat, col, res,N

    ## 끝까지 들어온거니까
    if r == N-1 :
        if pay < res:
            res = pay
        else :
            return
    else:
        if col[c] == 1:
            return

        else :
            col[c] = 1

            for i in range(N):
                if col[i] == 0 :
                    if pay + mat[r+1][i] < res:
                        go(r+1,i,pay+mat[r+1][i])

                        ## 들어갔다나오면 방문 되있으므로 방문 지움
                        col[i] = 0









import sys
sys.stdin = open('최소생산비용.txt','r')

for t in range(1,int(input())+1):
    N = int(input())
    mat = [ list(map(int,input().split())) for _ in range(N) ]




    ### 비용 합이 맥시멈
    res = 100 *  N


    for i in range(N):
        col = [0] * N
        go(0,i,mat[0][i])


    print(f'#{t} {res}')