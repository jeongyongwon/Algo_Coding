def search(s,dst):
    global start, end, data, res, last_dst

    if check[s]:
        return


    check[s] = 1
    x,y = data[s]

    ### 다 방문 했으면
    if sum(check) == len(check):
        last_dst = abs(x-end[0]) + abs(y-end[1])
        if res >  dst + last_dst :
            res = dst + last_dst
        else :
            return

    for i in range(len(data)):
        if check[i] == 0 :
            plus = abs(x-data[i][0]) + abs(y-data[i][1])
            if dst + plus < res :
                search(i,dst+plus)
                check[i] = 0




import sys
sys.stdin = open('최적경로.txt','r')

for t in range(1,int(input())+1):
    N = int(input())
    point = list(map(int,input().split()))

    start = None
    end = None


    data = []
    for i in range(0,len(point),2):
        if i == 0 :
            start = [point[i],point[i+1]]
        elif i == 2 :
            end = [point[i],point[i+1]]
        else :
            arr = [point[i],point[i+1]]
            data.append(arr)


    data.insert(0,start)
    start_index = 0
    last_dst = 0

    res = 20001
    check = [0] * len(data)
    search(0,0)
    print(f'#{t} {res}')
