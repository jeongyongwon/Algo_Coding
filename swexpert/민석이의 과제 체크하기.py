import sys
sys.stdin = open('민석이의 과제 체크하기.txt','r')
for t in range(int(input())):
    f, s = map(int,input().split())
    send = list(map(int,input().split()))

    all_ = []
    for i in range(1,f+1):
        all_.append(i)

    result = []
    for i in range(len(all_)):
        if all_[i] not in send:
            result.append(all_[i])

    result = map(str,result)
    print(f'#{t+1}',' '.join(result))
