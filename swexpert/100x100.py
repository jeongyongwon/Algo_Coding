import sys
sys.stdin = open('input.txt', 'r')


# T = 10
# for test in range(1, T+1):
#     no_meaning = int(input())
#     arr = []
     
#     for i in range(100):
#         arr.append(list(map(int, input().split())))
 
#     max_of_row = []
#     for i in range(100):
#         max_of_row.append(sum(arr[i]))
 
#     max_of_col = []
#     for i in range(100):
#         max_of_col.append(sum([arr[j][i] for j in range(100)]))
 
#     diagonal1 = 0
#     for i in range(100):
#         diagonal1 += arr[i][i]
 
#     diagonal2 = 0
#     for i in range(100):
#         diagonal2 += arr[-1-i][i]
 
#     answer_list = max_of_row + max_of_col + [diagonal1] + [diagonal2]
#     print('#{} {}'.format(test, max(answer_list)))







T = 10 
for t in range(1,T+1) :
    n_meaning = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int,input().split())))
    


    result = []
   

    # 행 합을 리스트에 추가
    for j in range(100) :
        result.append(sum(arr[j]))




    ## 열 합을 리스트에 추가
    for k in range(100) :
        cal = 0
        for l in range(100) :
            cal += arr[l][k]
        result.append(cal)

    ### 기울기1 대각선 합
    cal_1 = 0

    for a in range(100) :
        cal_1 += arr[a][a]
    result.append(cal_1)
    ### 기울기2 대각선 합

    c = 0
    d = 99
    cal_2 = 0
    while c < 100 :
        cal_2 += arr[c][d]
        c +=1
        d -=1
    result.append(cal_2)


    print(f'#{n_meaning} {max(result)}')