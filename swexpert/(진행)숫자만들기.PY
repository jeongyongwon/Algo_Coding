import sys
sys.stdin = open('숫자만들기.txt', 'r')


import itertools

for t in range(1,int(input())+1):
    N = int(input())
    cal = ['+', '-', '*', '/']
    cal_num = list(map(int,input().split()))
    cal_list = []
    for i in range(len(cal)):
        for j in range(cal_num[i]):
            cal_list.append(cal[i])

    num = list(map(int,input().split()))

    case_list = list(itertools.permutations(cal_list))
    print(case_list)


    












































