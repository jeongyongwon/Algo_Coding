import sys
sys.stdin = open('Forth.py.txt','r')



T = int(input())
for t in range(T):
    num = list(input().split())
    cal_list = ['+','-','*','/','.']
    stack = []
    cnt = 0
    for  i in num :
        if i not in cal_list:
            cnt += 1

    is_end = True
    i = 0
    while is_end :
        if cnt == len(num):
            is_end = False
            print(f'#{t+1} error')

        if num[-1] not in cal_list:
            is_end = False
            print(f'#{t+1} error')

        if num[i] not in  cal_list  :
            stack.append(int(num[i]))
        else : ## 연산자일 때

            if num[i] == '.':
                is_end = False
                print(f'#{t+1} {stack[0]}')


            if num[i] == '+':
                if len(stack) <= 1:
                    is_end = False
                    print(f'#{t+1} error')
                else :
                    new_ = stack[-1] + stack[-2]
                    del stack[-1]
                    del stack[-1]
                    stack.append(new_)


            if num[i] == '-':
                if len(stack) <= 1:
                    is_end = False
                    print(f'#{t+1} error')
                else:
                    new_ = stack[-2] - stack[-1]
                    del stack[-1]
                    del stack[-1]
                    stack.append(new_)

            if num[i] == '*':
                if len(stack) <= 1:
                    is_end = False
                    print(f'#{t+1} error')
                else:
                    new_ = stack[-1] * stack[-2]
                    del stack[-1]
                    del stack[-1]
                    stack.append(new_)

            if num[i] == '/':
                if len(stack) <= 1:
                    is_end = False
                    print(f'#{t+1} error')
                else:
                    new_ = stack[-2] // stack[-1]
                    del stack[-1]
                    del stack[-1]
                    stack.append(new_)
        i += 1

