def sea(r,count):
    global check, rel, N, M,  cnt, no

    if check[r]:
        return

    check[r] = 1

    if count == 1:
        return

    for i in range(2,N+1):
        if rel[r][i] == 1 and check[i] == 0 and rel[1][i] == 0 :
            cnt += 1
            sea(i,count+1)


import sys
sys.stdin = open('상원이의생일파티.txt','r')

for t in range(1,int(input())+1):
    N, M = map(int,input().split())

    rel = [[0] * (N+1) for _ in range(N+1)]
    ### 1번은 상원이 / 이새킨 친구가 없을 수도 있음
    for i in range(M):
        s, e = map(int,input().split())
        rel[s][e] = 1
        rel[e][s] = 1

    check = [0] * (N+1)

    no = False
    cnt = 0
    if sum(rel[1]) == 0 :
        print(f'#{t} {cnt}')
    else :
        for i in range(2,N+1):
            if rel[1][i] != 0 :
                cnt += 1
                sea(i,0)


        print(f'#{t} {cnt}')



