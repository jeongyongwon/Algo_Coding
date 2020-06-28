import sys
sys.stdin = open('파리퇴치.txt', 'r')

T = int(input())
for t in range(T) :
    N, M = list(map(int,input().split()))
    matrix_ = [ ]
    for n in range(N) :
        matrix_.append(list(map(int, input().split())))

    result = []

    for i in range(N-M+1):
        for j in range(N-M+1) :
            cal = 0
            for k in range(M) :
                cal += sum(matrix_[i+k][j:j + M])
            result.append(cal)






    print(f'#{t+1} {max(result)}')




