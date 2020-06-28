def go(index,cnt,eng):
    global  res, charge

    ## 도착점 이상으로 갈 수 있으면 끝내면 됨
    if index >= charge[0]:
        if cnt < res :
            res = cnt
        else :
            return

    else :
        ### engine에 에너지 채우기

        ###  만약 지금 가진 에너지와 인덱스로 더했을 때 갈 수 있는 것을 알면 밑에 재귀를 할 필요가 없다
        if eng + index >= charge[0]:
            if cnt+1 < res:
                res = cnt+1
            else:
                return


        else:
            ## 에너지는 1부터 eng 에너지 남은거 까지 더할 수 있으므로
            for i in range(1,eng+1):
                if res > cnt + 1:
                    go(index+i ,cnt+1,eng-i+charge[index+i])




import sys
sys.stdin = open('전기버스2.txt','r')

for t in range(1,int(input())+1):
    charge = list(map(int,input().split()))
    ## 1번은 무조건 시작해야함



    ### 정류장의 개수 이상으로 교환 횟수가 나올 수는 없으므로
    res = charge[0]

    go(1,-1,charge[1])

    print(f'#{t} {res}')