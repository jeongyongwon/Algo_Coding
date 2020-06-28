import sys
sys.stdin = open('삼성시의버스노선.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    way = []
    bus_stop = [0  for _ in range(5000)]
    for i in range(N):
        a = list(map(int,input().split()))
        for j in range(a[0], a[1]+1):
            bus_stop[j-1] += 1

    result = []
    P = int(input())
    for i in range(P):
        way.append( str(bus_stop[ int(input())-1]))


    print(f'#{t+1}',' '.join(way) )

