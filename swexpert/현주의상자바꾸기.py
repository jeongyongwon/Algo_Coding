import sys
sys.stdin = open('현주의상자바꾸기.txt','r')

for t in range(int(input())):
    N, Q = map(int,input().split())

    box = [0 for _ in range(N)]
    for i in range(1,Q+1):
        L,R = map(int,input().split())
        for j in range(L-1,R):
            box[j] = i


    box = list(map(str,box))
    print(f'#{t+1}',' '.join(box))

