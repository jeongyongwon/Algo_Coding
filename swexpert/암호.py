import sys
sys.stdin = open('암호.txt','r')

for t in range(1,int(input())+1):
    N, M, K = map(int,input().split())
    num_list = list(map(int,input().split()))

    is_end = True
    start = 0
    last_plus_index = 0


    while is_end :
        start += 1
        last_plus_index = last_plus_index + M

        if last_plus_index < len(num_list):
            num_list.insert(last_plus_index,num_list[last_plus_index]+num_list[last_plus_index-1])

        elif last_plus_index == len(num_list):
            num_list.append(num_list[-1] + num_list[0])
            last_plus_index = -1

        else:
            last_plus_index = last_plus_index - len(num_list)
            num_list.insert(last_plus_index,num_list[last_plus_index]+num_list[last_plus_index-1])





        if start == K :
            is_end = False
            break




    if len(num_list) > 10 :
        print(f'#{t}',end=' ')
        for i in range(len(num_list)-1,len(num_list)-11,-1):
            print(num_list[i],end=' ')
        print("")
    else :
        print(f'#{t}', end=' ')
        for i in range(len(num_list)-1,-1,-1):
            print(num_list[i],end=' ')
        print("")