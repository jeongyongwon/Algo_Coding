


import sys
sys.stdin = open('공통조상.txt','r')


def FindUp(start):
    global ans_p
    root = cur = start
    p = tree[root][1]
    cnt = 0
    Visited = [0] * (V + 1)
    v = 0
    while True:
        if cur == p:
            break
        for n in tree[cur][0]:
            if not Visited[n]:
                cur = n
                break
        else:
            if cur == C1 or cur == C2:
                cnt += 1
            Visited[cur] = 1
            v += 1
            cur = tree[cur][1]
    if cnt == 2:
        return v


for tc in range(1, int(input()) + 1):
    V, E, C1, C2 = map(int, input().split())
    tree = [[[], 0] for _ in range(V + 1)]
    E_list = list(map(int, input().split()))
    for e in range(0, E * 2, 2):
        tree[E_list[e]][0].append(E_list[e + 1])
        tree[E_list[e + 1]][1] = E_list[e]
    ans_p = 0
    ans_s = 0
    r = 1
    v = V
    while FindUp(r):
        for n in tree[r][0]:
            if FindUp(n):
                r = n
                v = FindUp(r)
                break
        else:
            break
    print('#%d' % tc, r, v)

    print(tree)
