import sys
sys.stdin = open('의석이의세로로말해요.txt', 'r')

T = int(input())
for t in range(T):
    f_list = []
    for n in range(5):
        f_list.append(  list(input().split()))

    result = []
    for i in range(len(f_list)):
        test = []
        for j in f_list[i][0] :
            test.append(j)
        result.append(test)

    max_len = 0
    for k in range(len(result)) :
        if len(result[k]) > max_len :
            max_len = len(result[k])
        else :
            pass

    for l in range(len(result)) :
        result[l] += [None] * (max_len - len(result[l]))


    result_text = ''

    for a in range(len(result[0])) :
        for b in range(len(result)) :
            if result[b][a] == None :
                pass
            else :
                result_text += result[b][a]
    print(f'#{t+1} {result_text}')


