import sys
sys.stdin = open('컨테이너운반.txt','r')

T = int(input())
for t in range(1, 1+T):
    N, M = map(int, input().split())
    container = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    result = 0
    i = 0
    while container and truck:
        if container[i] <= truck[i]:
            result += container[i]
            container.remove(container[i])
            truck.remove(truck[i])
        else:
            container.remove(container[i])
    print('#{} {}'.format(t, result))