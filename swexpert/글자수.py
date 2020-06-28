import sys
sys.stdin = open('글자수세기.txt', 'r')

T = int(input())

for t in range(T):
    str1 = input()
    str2 = input()

    result = 0

    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j] :
                cnt += 1
            else :
                pass

        if cnt > result :
            result = cnt


    print(f'#{t+1} {result}')
