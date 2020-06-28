import sys
sys.stdin = open('subtree.txt','r')

for t in range(1,int(input())+1):
    E, start = map(int,input().split())
    list_ = list(map(int,input().split()))

    tree = [[] for _ in range(E+2)]

    for i in range(0,len(list_),2):
        tree[list_[i]].append(list_[i+1])


    cnt = 0
    visited = [0 for _ in range(E+2)]

    def search(r):

        global cnt
        global visited
        global tree

        if visited[r] :
            return

        visited[r] = 1
        cnt += 1

        if len(tree[r]) == 0:
            return
        else :
            for i in range(len(tree[r])):
                search(tree[r][i])

    search(start)
    print(f'#{t} {cnt}')