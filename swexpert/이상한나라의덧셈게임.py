import sys
sys.stdin = open('이상한나라의덧셈게임.txt','r')

for t in range(1,int(input())+1):
    num = list(input())
    ### A가 엘리스 B가 토끼
    ### 받았을 때 한자리이면 패배

    start = 0
    is_end = True
    ### 게임횟수가 홀수에서 끝날 때 토끼 승(B) / 짝수 일때 엘리스 승(A)
    while is_end :

        ### 끝내는 과정
        start += 1
        if len(num) == 1:
            is_end = False
            if start % 2 == 1:
                print(f'#{t} B')

            else :
                print(f'#{t} A')
            break

        change = 0 ## 숫자 연산
        point = 0 ## 연산으로 인한 숫자를 집어넣을 지점


        ### 게임에 최선을 다해야하므로 연산으로 인한 최대값을 찾음
        for i in range(len(num)-1):
            if int(num[i]) + int(num[i+1])  > change:
                change = int(num[i]) + int(num[i+1])
                point = i
            else :
                pass

        ####
        if len(str(change))>= 2:
            change_list = list(str(change))
            if point == 0:
                for i in range(len(change_list)-1,-1,-1):
                    num.insert(1,change_list[i])
                del num[3]
                del num[0]

            else :
                num[point+1 : 0 ] = change_list
                del num[point+3]
                del num[point]


        else :
            num.insert(point, str(change))
            del num[point + 1: point + 3]











