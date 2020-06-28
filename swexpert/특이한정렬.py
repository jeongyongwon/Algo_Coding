import sys

sys.stdin = open('특이한정렬.txt', 'r')





T = int(input())
for t in range(T) :
    len_num = int(input())
    num_list = input().split()
    num_list = list(map(int,num_list ))
    list_up = sorted(num_list)
    list_do = list(reversed(list_up))

    is_remove = True
    result = [ ]
    while is_remove :
        result.append(list_up[-1] )
        list_up.remove(list_up[-1] )
        result.append(list_up[0])
        list_up.remove(list_up[0])
        if len(list_up) == 0 :
            is_remove = False
        else :
            pass
    print(f'#{t+1} {result[0]} {result[1]} {result[2]} {result[3]} {result[4]} {result[5]} {result[6]} {result[7]} {result[8]} {result[9]}')




