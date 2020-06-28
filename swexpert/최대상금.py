import sys
sys.stdin = open('최대상금.txt','r')

for t in range(1,int(input())+1):
    ### 인덱스 0에서 가중치는 인덱스 * 10^n이다
    num, change = input().split()
    ### 정수형 변환
    change = int(change)
    num = list(num)




    for i in range(len(num)):
        num[i] = int(num[i])



    start = 0
    cnt = 0
    the_end = True

    _max = max(num)
    cnt_m = 0
    arr_i = []
    for i in range(len(num)):
        if _max == num[i]:
            cnt_m += 1
            arr_i.append(i)





    while the_end:

        if change == cnt :
            the_end = False
            break
        elif len(num) <= 0 :
            the_end = False
            break
        else:
        ### 교환 횟수 카운트
            if start >= len(num):

                the_end = False
                break


            else :

                iv = 0
                index = 0
                is_end2 = True
                value = -1
                while is_end2 :
                    if index+start >= len(num):
                        is_end2 = False
                        break

                    elif num[index+start] >= value :
                        value = num[index+start]
                        iv = index+start

                    index += 1
                if iv == start :
                    pass

                else :
                    i_value = num.pop(iv)
                    a_value = num.pop(start)

                    num.insert(start,i_value)
                    if cnt_m > change:
                        num.append(a_value)
                    else :
                        num.insert(iv, a_value)


                    # num[start], num[iv] = num[iv], num[start]
                    cnt += 1

            start += 1

    ### max 값이 cnt가 교환횟수 이상일 때 처리해줘야함
    if cnt != change:
        while cnt != change :
            if cnt_m > 1 :
                cnt += 1
            else :
                num[len(num)-1],  num[len(num)-2] = num[len(num)-2],  num[len(num)-1]
                cnt += 1
        res = ''.join(list(map(str, num)))
        print(f'#{t} {res}')
    else :
        res = ''.join(list(map(str, num)))
        print(f'#{t} {res}')
    print(cnt_m)








