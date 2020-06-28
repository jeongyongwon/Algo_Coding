import sys
sys.stdin = open('새샘이와세소수.txt','r')





## 소수는 1과 자기 자신만 나누어지는 수임
for t in range(int(input())):
    num = int(input())
    count = 0
    sosu_list = []


    for i in range(2, num + 1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0 :
                cnt += 1
        if cnt == 2:
            sosu_list.append(i)

    for i in range(len(sosu_list)) :
        if sosu_list[i] > num :
            break
        else:
            for j in range(i,len(sosu_list)):
                if sosu_list[i]+sosu_list[j] > num:
                    break
                else :
                    for k in range(j,len(sosu_list)):
                        if sosu_list[i] + sosu_list[j] + sosu_list[k] > num:
                            break
                        elif sosu_list[i] + sosu_list[j] + sosu_list[k] == num:
                            count += 1


    print(f'#{t+1} {count}')
