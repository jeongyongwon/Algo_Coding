import sys, math
sys.stdin = open('하나로.txt','r')

for t in range(1,int(input())+1):
    N = int(input())
    ### 두섬과의 거리는 sqrt(dx^2 + dy^2 )
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))

    E = float(input())
    res = 0

    ## max distance로 비교하기


    for i in range(N):

        ### max distance
        x_dst = 1000000
        y_dst = 1000000



        is_end = True
        len_cnt = i

        
        ### 어떤 점이 연결되는지 표시하기 위함
        p_1 = 0
        p_2 = 0
        while is_end :
            ### x -> y 랑 y - > x 겹치는 경우는 제외해줘야함


            ### 한 섬에 하나만 연결하는 것은 아니므로  여러개 연결해도 됨

            len_cnt +=1
            if len_cnt == N :
                is_end = False
                ### 한바퀴 다돌리고  검증한 점들의 거리를 res에 더해줌
                if x_dst == 1000000 and y_dst == 1000000:
                    break
                else :
                    res += round((x_dst ** 2 + y_dst ** 2) * E)

                    break

            else :
                if (x[len_cnt] - x[i])**2 + (y[len_cnt] - y[i])**2 < (x_dst**2) + (y_dst)**2 :
                    ### 작으면 좌표를 교체 해준다
                    x_dst = x[len_cnt] - x[i]
                    y_dst = y[len_cnt] - y[i]

                    p_1 = i
                    p_2 = len_cnt



    # print(f'#{t} {res}')

    print(res)

