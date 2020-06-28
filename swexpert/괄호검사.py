import sys
sys.stdin = open('괄호검사.txt', 'r')

t = int(input())
for tt in range(t):
    text_ = input()

    list_ = []
    for i in text_ :
        if i == '{' or i == '}' or i == '(' or i == ')' :
            list_.append(i)


    cnt1, cnt2, cnt3, cnt4 = 0,0,0,0
    for i in list_ :
        if  i == '{' :
            cnt1 += 1
        elif i == '}':
            cnt2 += 1
        elif i == '(':
            cnt3 += 1
        elif i == ')':
            cnt4 += 1

    if cnt1 == cnt2 and cnt3 == cnt4 :
        print(f'#{tt+1} 1')
    else :
        print(f'#{tt+1} 0')

