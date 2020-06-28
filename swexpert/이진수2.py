import sys
sys.stdin = open('이진수2.txt','r')

for t in range(1,int(input())+1):
    num = float(input())


    o_cnt = 0
    binary = ''
    is_end = True
    while is_end :
        if num == 1:
            is_end =False
            break

        if o_cnt >= 13:
            is_end = False
            binary ='overflow'
            break


        cal = int(num * 2)
        binary += str(cal)
        o_cnt += 1
        if num * 2 > 1:
            num = num * 2 - 1
        else :
            num = num * 2


    print(f'#{t} {binary}')
