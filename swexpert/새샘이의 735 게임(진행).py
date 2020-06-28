import sys
sys.stdin = open('새샘이735.txt', 'r')

for t in range(int(input())):
    num = list(map(int,input().split()))
    print(num)


    for a in num:
        for b in num:
            if a==b :
                break
            else:
                for c in num:


