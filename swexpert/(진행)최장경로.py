def dfs(r,cnt):
    global cnt_res
    global visit
    global N
    global mat

    if visit[r]:
        return
    visit[r] = 1


    for i in mat[r]:
        not_cnt = 0
        if visit[i] == 0:
            not_cnt += 1
            dfs(i,cnt+1)
        if not_cnt == 0 :
            if cnt_res < cnt :
                cnt_res = cnt







import sys
sys.stdin = open('최장경로.txt','r')
for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    mat = [ [] for _ in range(N+1)]



    for i in range(M):
        a,b = map(int,input().split())
        mat[a].append(b)
        mat[b].append(a)

    cnt_res = 0

    visit = [0 for _ in range(N+1) ]

    for i in range(1,N+1):
        dfs(i,1)

    if cnt_res == 0 :
        print(f'#{t} 1')
    else :
        print(f'#{t} {cnt_res}')















