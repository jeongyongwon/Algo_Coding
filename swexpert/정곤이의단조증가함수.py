import sys
sys.stdin = open('정곤이의단조증가함수.txt', 'r')


### 우선 곱했을 대 단조 증가 인수를 구하기
### 그 다음 최대값 구하지
T = int(input())
for t in range(T):
    N = int(input())
    num_list = list(map(int,input().split()))

    plus_list = []

    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)) :
            if len(str(num_list[i] * num_list[j])) == 1:
                pass
            else:
                plus_list.append(str(num_list[i] * num_list[j]))



    prove_list = [0] * len(plus_list)

    for a in range(len(plus_list)) :
        for b in range(len(plus_list[a])-1) :
            if plus_list[a][b] > plus_list[a][b+1]:
                prove_list[a] += 1
            else :
                pass

    max_ = -1
    for c in range(len(prove_list)):
        if prove_list[c] == 0 :
            if int(plus_list[c]) > max_ :
                max_ =  int(plus_list[c])
            else:
                pass
        else :
            pass



    print(f'#{t+1} {max_}')

















