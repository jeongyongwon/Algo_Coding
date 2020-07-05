def backtracking(list_, check_, null_list,cnt):
    global per_list
    global burger

    if len(null_list) == cnt:
        sub_list = []
        for k in null_list:
            sub_list.append(k)

        isCan = 0

        for ham in burger:
            ## 안되는 리스트 가져오기

            isin = 0
            for not_ in ham:
                if not_ in sub_list:
                    isin += 1
            if len(ham) == isin:
                isCan += 1
                break
        if isCan == 0 :
            if set(sub_list) in per_list:
                pass
            else :
                per_list.append(set(sub_list))
        else :
            return

    else:
        for i in range(len(list_)):
            if check_[i]:
                pass
            else:
                check_[i] += 1
                null_list.append(list_[i])
                backtracking(list_, check_,null_list,cnt)
                check_[i] -= 1
                null_list.pop()

def permutate(leng,select):
    global back_list

    ## 이걸 사용했는지
    check = [0] * leng

    ### 숫자들 리스트
    num = list(range(1,leng+1))
    arr_null = []
    backtracking(num,check,arr_null,select)


import sys
sys.stdin = open('수제버거장인.txt','r')

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    burger = []
    ##재료의 종류는 1~N까지
    ## M개 안되는 쌍
    for m in range(M):
        li = list(map(int,input().split()))
        burger.append(li)


    ### 순열 케이스 분류

    per_list = []

    for i in range(N+1):

        permutate(N,i)

    per_list[0] = 0
    print(f'#{t} {len(per_list)}')
