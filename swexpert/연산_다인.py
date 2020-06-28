import sys
from collections import deque
sys.stdin = open('연산.txt', 'r')

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    q = deque()
    q.appendleft([N, 0])
    result = 0
    is_end = True
    visit = {}

    while is_end:
        queue = q.popleft()

        if queue[0] == M:
            is_end = False
            result = queue[1]
            break
        else :

            for x in range(4):
                if x == 0:
                    result = queue[0] + 1
                elif x == 1:
                    result = queue[0] - 1
                elif x == 2:
                    result = queue[0] * 2
                elif x == 3:
                    result = queue[0] - 10

                if result == M:
                    stop = True
                    print('#{} {}'.format(test, queue[1]+1))
                    break

                else :
                    ### KeyError가 뜬 다는 것은 없다는 것이므로 추가
                    try:
                        if visit[result] < queue[1] + 1:
                            visit[result] = queue[1] + 1
                            q.append([result, queue[1] + 1])

                    except KeyError:
                        visit[result] = queue[1] + 1
                        q.append([result, queue[1] + 1])





