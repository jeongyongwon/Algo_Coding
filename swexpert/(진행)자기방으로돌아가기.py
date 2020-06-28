import sys
sys.stdin = open('자기방으로돌아가기.txt','r')

for t in range(1,int(input())+1):
    N = int(input())
    way = []
    for i in range(N):
        way.append(list(map(int,input().split())))

    room = [0 for _ in range(401)]
    cnt = 0



    for i in range(N):
        for j in range(way[i][0], way[i][1]+1):
            room[j] += 1



    # for a,b in way :
    #     time += 1
    #     if sum(room[a:b+1])/(b-a+1) == 1 :
    #         cnt += 1
    #     else :
    #         div_cnt += 1
    #
    #












