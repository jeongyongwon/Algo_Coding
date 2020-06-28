import sys
sys.stdin = open('다솔이의월급상자.txt','r')
T = int(input())
for t in range(T):
    leng = int(input())
    per = 0
    for i in range(leng):
        a = list(input().split())
        per += float(a[0]) * int(a[1])


    print(f'#{t+1}','%0.6f' % per)
