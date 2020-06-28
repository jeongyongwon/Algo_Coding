import sys
sys.stdin = open('무선단속카메라.txt','r')

for t in range(1,int(input())+1):
    N = int(input()) ## 카메라 개수
    K = int(input()) ## 수신기 개수

    point = list(set(map(int,input().split())))

    far = []
    for i in range(1,len(point)):
        far.append(point[i] - point[i-1])





    for i in range(K-1):
        D = max(far)
        del far[far.index(D)]


    print(f'#{t} {sum(far)}')