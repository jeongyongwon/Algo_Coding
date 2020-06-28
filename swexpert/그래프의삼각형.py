import sys
sys.stdin = open('그래프의삼각형.txt', 'r')

for t in range(int(input())):
    n, m = map(int,input().split())
    line_ = []
    for i in range(m):
        line_.append(list(map(int,input().split())))



    ## 어떤 점을 뽑았을 때 3개의 점중 x 좌표가 같은거 2개, y좌표가 같은거 2개  x,y 같은거 1개
    cnt = 0
    for i in range(len(line_)):
        for j in range(len(line_)):
            if i != j :
                for k in range(len(line_)):
                    if i != k or j != k :
                        if line_[i][0] == line_[j][0] and line_[j][1] == line_[k][1] and line_[i][1] == line_ [k][0] :
                            cnt += 1



    print('#{} {}'.format(t+1,cnt))