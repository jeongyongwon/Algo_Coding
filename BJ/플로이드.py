import sys
sys.stdin = open('플로이드.txt','r')

n = int(input())
m = int(input())

info = []

for i in range(m):
    start, end, pay = map(int,input().split())
    info.append([start, end, pay])

### 출발지점 / 도착 지점 / 비용
print(info)