import sys
sys.stdin = open('최소값으로이동하기.txt','r')

for t in range(1,int(input())+1):
    W,H,N = map(int,input().split())

    pot = []
    for i in range(N):
        x, y = map(int,input().split())
        test = [x,y]
        pot.append(test)


    ## CASE 분류
    # 행은 같고 열은 다를 때
    # 열은 같고 행은 다를 때
    # 둘 다 다를 때
    pay = 0
    start = 0
    is_end = True
    while is_end:
        ## 좌표 잡아주기
        c2, r2 = pot[start+1][0],pot[start+1][1]
        c1, r1 = pot[start][0], pot[start][1]

        is_end2 = True

        while is_end2:
            if r2 == r1 and c2 == c1 :
                is_end2 = False
                break
            elif r2 > r1 and c2 > c1 :  ## 무조건 위에 있을 경우
                r1 = r1 + 1
                c1 = c1 + 1
                pay += 1
            elif r2 == r1 and c2 > c1 : ## 열만 상위인 경우
                c1 = c1 + 1
                pay += 1
            elif r2 > r1 and c2 == c1 : ## 행만 상위인 경우
                r1 = r1 + 1
                pay += 1

            elif r2 < r1 and c2 < c1 :
                r1 = r1 - 1
                c1 = c1 - 1
                pay += 1

            elif r2 < r1 and  c2 == c1:
                r1 = r1 - 1
                pay += 1
            elif r2 == r1 and c2 < c1:
                c1 = c1 - 1
                pay += 1

            elif r2 > r1 and c2 < c1 :
                r1 = r1 + 1
                c1 = c1 -1
                pay += 2

            elif r2 < r1 and c2 > c1:
                r1 = r1 - 1
                c1 = c1 + 1
                pay += 2

        start += 1
        if start == len(pot)-1:
            is_end = False
            break

    print(f'#{t} {pay}')