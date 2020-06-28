def dfs(r,cnt):
    global check, mat, res


    for i in range(N):
        if check[i] == False and cnt+mat[r][i] < res:
            check[r] = True
            dfs(i,cnt+mat[r][i])
            check[i] = False

    if sum(check.values()) == len(check) :
        val = cnt + mat[r][0]
        if val < res :
            res = val



import sys
sys.stdin = open('전자카트.txt','r')

for t in range(1,int(input())+1):
    N = int(input())
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))

    check = {}
    for i in range(N):
        check[i] = False
    check[0] = True

    res = 1000

    dfs(0,0)

    print(f'#{t} {res}')