import sys
sys.stdin = open('노드의합.txt','r')

for t in range(1,int(input())+1):
    N, M, L = map(int,input().split())
    ### 노드의 개수 / 리프 노드의 개수 / 출력 노드 번호
    ## 완전이진트리
    tree = [0 for _ in range(N+1)]

    for i in range(M):
        node, num = map(int,input().split())
        tree[node] = num


    for i in range(len(tree)-1,0,-1):
        if tree[i] == 0:
            if 2*i >= len(tree) and 2*i + 1 >= len(tree) :
                break
            elif 2*i + 1 >= len(tree) :
                tree[i] = tree[2*i]
            else :
                tree[i] = tree[2*i] + tree[2*i + 1]


        else :
            pass

    print(f'#{t} {tree[L]}')