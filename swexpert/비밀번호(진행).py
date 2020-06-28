import sys
sys.stdin = open('비밀번호.txt', 'r')

T = 10
for t in range(T):
    leng, num = input().split()
    leng = int(leng)
    num = list(num)
    i = 0
    is_end = True
    while is_end :
        if i == len(num) - 1:
            is_end = False
        elif  num[i] != num[i+1] :
            i += 1
        elif num[i] == num[i+1] : ## 같은 처음 지점을 찾으면
            is_end2 = True
            j = 0
            while is_end2 :
                j += 1
                if  i-j <= -1 or i+1+j >= len(num) :
                    j -= 1
                    is_end2 = False
                elif num[i-j] == num[i+1+j] :
                    pass

                elif  num[i-j] != num[i+1+j] :
                    j -= 1
                    is_end2 = False
            del(num[i-j:i+j+1+1])
            i = 0
        else :
            is_end = False

    print(f'#{t+1}',''.join(num))





