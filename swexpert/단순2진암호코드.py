import sys

sys.stdin = open('단순2진암호코드.txt','r')

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    num = []
    for i in range(N):
        num.append(input())

    ### 번호 리스트 뽑아내고
    for i in range(len(num)):
        if '1' in num[i]:
            binary_list = num[i]
            break

    print(binary_list)

    start = 0
    end = 0

    for i in range(len(binary_list)):
        if binary_list[i] == '1' :
            start = i - 1
            break


    
