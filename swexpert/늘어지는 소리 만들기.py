import sys
sys.stdin = open('늘어지는소리만들기.txt','r')

for t in range(1,int(input())+1 ):
    text = list(input())
    H = int(input())
    place = list(map(int,input().split()))

    a = dict()

    for i in range(len(text)+1):
        a[i] = 0

    for i in place :
        a[i] += 1


    for i,j in a.items():

        if j == 0:
            pass
        else :
            if i == 0:
                text[i] = '-'*j + text[i]
            else:
                text[i-1] += '-'* j

    print('#{} {}'.format(t,''.join(text)))



