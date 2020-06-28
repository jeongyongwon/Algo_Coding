import sys
sys.stdin = open('햄버거 다이어트.txt','r')

for t in range(int(input())):
    N, L = map(int,input().split()) ## 재료수, 제한 칼로리
    score = []
    cal = []
    for i in range(N): ## 점수, 칼로리
        a, b = map(int,input().split())
        score.append(a)
        cal.append(b)

    ## L보다 점수 작으면서
    ## score max
    max_score = 0




