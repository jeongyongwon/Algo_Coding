import sys
sys.stdin = open('문자열비교.txt', 'r')


T = int(input())
for t in range(T):
    str1 = input()
    str2 = input()
    cnt = 0
    for i in range(len(str2) - len(str1)) :
        if str1 == str2[i:i+len(str1)]:
            cnt += 1
        else :
            pass

    if cnt == 0 :
        pass
    if cnt > 1 :
        cnt = 1

    print(f'#{t+1} {cnt}')



    ## str2.__contains__(str1) ### str2안에 str1이 포함된다면 True 출력

