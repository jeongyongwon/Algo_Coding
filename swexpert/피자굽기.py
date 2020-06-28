import sys
sys.stdin = open('피자굽기.txt','r')


for t in range(1,int(input())+1):
    # N이 화덕크기 , M이 피자개수
    N,M = map(int,input().split())
    pizza = list(map(int,input().split()))
    fire = []

    pizza_num = list(range(M))
    num_queue = []

    melting_cheeze = [[0] for _ in range(M)]
    is_end = True


    result = 0

    ### 우선 피자를 순서대로 넣는거임
    ### 다녹은 피자는 없애고 num도 없애자


    while is_end :
        if len(fire) != N : ## 화덕이 가득 안 채워졌다면 계속 채워넣기
            if len(pizza) == 0 :
                fire[0] = fire[0] // 2
                if fire[0] == 0:
                    ### 치즈가 0이 됬을 떄 그냥 pop만  해버림  / num도 pop해야함
                    fire.pop(0)
                    num_queue.pop(0)
                    ## pop을 했을 때 화덕에 한개가 남았다면 그게 마지막 피자임
                    if len(fire) == 1:
                        result = num_queue[0]
                        is_end = False
                        break

                else:
                    ## 치즈가 0이 아닐 경우 다시 맨 뒤로 보냄
                    last_fire = fire.pop(0)
                    fire.append(last_fire)

                    last_num = num_queue.pop(0)
                    num_queue.append(last_num)


            else :
                first_pizza = pizza.pop(0)
                fire.append(first_pizza)

                first_num = pizza_num.pop(0)
                num_queue.append(first_num)

        elif len(fire) == N :
            fire[0] = fire[0]//2
            if fire[0] == 0 :
                ### 치즈가 0이 됬을 떄 그냥 pop만  해버림  / num도 pop해야함
                fire.pop(0)
                num_queue.pop(0)
                ## pop을 했을 때 화덕에 한개가 남았다면 그게 마지막 피자임
                if len(fire) == 1 :
                    result = num_queue[0]
                    is_end = False
                    break

            else :
                ## 치즈가 0이 아닐 경우 다시 맨 뒤로 보냄
                last_fire = fire.pop(0)
                fire.append(last_fire)

                last_num = num_queue.pop(0)
                num_queue.append(last_num)


        else :
            pass




    print(f'#{t} {result+1}')










