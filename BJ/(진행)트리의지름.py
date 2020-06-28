

import sys
sys.stdin = open('트림의지름.txt','r')

N = int(input())

tree = [ [] for _ in range(N+1) ]

visited = [[0] * (N+1)  for _ in range(N+1) ]

for i in range(N-1):
    parent, child, plus = map(int, input().split())
    tree[parent].append(child)
    visited[parent][child] += plus

for i in range(N+1):
    print(visited[i])


res = 0
sub_res = 0


print(tree)




