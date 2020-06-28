import sys
sys.stdin = open('올림픽종목투표.txt','r')

for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    vote = [0 for _ in range(N)]


    for i in range(M): ## 위원회
        for j in range(N): ## 종목
            if B[i] < A[j]:
                pass
            if B[i] >= A[j]:
                vote[j] += 1
                break

    print('#{} {}'.format(t,vote.index(max(vote))+1 ))
