import sys
sys.stdin = open('수열합치기.txt','r')


for t in range(1,int(input())+1):
    N, M = map(int,input().split())


    first_list = list(map(int,input().split()))
    for i in range(M - 1):
        list_plus = list(map(int, input().split()))

        start = 0
        is_end = True
        while is_end:
            if start >= len(first_list):
                first_list.extend(list_plus)
                is_end = False
                break

            if first_list[start] > list_plus[0]:
                first_list[start:0] = list_plus
                is_end = False
                break

            else:
                start += 1



    print('#{} '.format(t), end='')
    first_list = first_list[::-1]
    for i in range(10):
        print(first_list[i], end=' ')
    print()


