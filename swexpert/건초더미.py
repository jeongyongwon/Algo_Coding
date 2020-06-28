import sys
sys.stdin = open('건초더미.txt','r')

T = int(input())
for t in range(T):
    n = int(input())
    mow = []
    for nn in range(n):
        mow.append(int(input()))

    final_ = int(sum(mow)/len(mow))
    gap = []
    for i in range(len(mow)):
        gap.append(mow[i] - final_)


    result = 0
    for i in gap:
        if i > 0 :
            result += i
        else :
            pass

    print(f'#{t+1} {result}')
