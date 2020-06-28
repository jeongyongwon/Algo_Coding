import sys
sys.stdin = open('제곱수의합계산하기.txt','r')

for t in range(1,int(input())+1):
    N = int(input())
    nums = list(input().split())

    res = 0
    for num in nums:
        sq_num = int(num[-1])
        cal_num = int(num[0:len(num)-1])
        res += cal_num**sq_num



    print(f'#{t} {res}')
