import sys
sys.stdin = open('백만장자프로젝트.txt', 'r')


T = int(input())
for t in range(T) :
    n = int(input())
    p = list(map(int,input().split()))

    benefit_ = 0
    pay = 0
    cnt = 0
    for i in range(len(p)):
        if i < len(p) - 1 :
            if p[i] <= max(p[i+1:]) :
                pay += p[i]
                cnt += 1
            elif p[i] > max(p[i+1:]):
                benefit_ += (p[i] * cnt) - pay
                cnt = 0
                pay = 0

        else :
            if p[i-1] <= p[i] :
                benefit_ += (p[i] * cnt) - pay
            else:
                pass



    print(f'#{t+1} {benefit_}')

## 핵심은 저렴할 때마다 사서 비쌀 때 파는 것이다.



