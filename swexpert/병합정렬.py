import sys
sys.stdin = open('병합정렬.txt','r')


for t in range(1,int(input())+1):
    N = int(input())
    num = list(map(int,input().split()))
    # num_1 = num[0:N//2]
    # num_2 = num[N//2 : ]

    cnt_1 = 0
    cnt_2 = 0
    print(num)

    i = 0
    plus = 0
    weight = 0
    is_end = True
    while is_end :

        plus += 2
        weight += 1

        for i in range(0,len(num)//plus):
            if num[i] > num[i+weight]:
                cnt_1 += 1
            elif num[i] < num[i+weight] :
                cnt_2 += 1







