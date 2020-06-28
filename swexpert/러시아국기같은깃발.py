import sys
sys.stdin = open('러시아국기같은깃발.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    cnt = 0
    mm = 2501
    for j in range(len(board[0])):
        if board[0][j] != 'W':
            cnt += 1
    for j in range(len(board[-1])):
        if board[-1][j] != 'R':
            cnt += 1
    for i in range(1, N-1):
        for j in range(1, N-i):
            result = 0
            for k in range(1, j):
                for m in range(M):
                    if board[k][m] != 'W':
                        result += 1
            for k in range(j, j+i):
                for m in range(M):
                    if board[k][m] != 'B':
                        result += 1
            for k in range(j+i, N-1):
                for m in range(M):
                    if board[k][m] != 'R':
                        result += 1
            if result < mm:
                mm = result
    print("#{} {}".format(tc, mm+cnt))








