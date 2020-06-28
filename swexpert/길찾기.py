def dfs(n):
    if visited[n] :
        return
    visited[n] = 1

    print(n, end=' ')

    for k in mat[n] :
        if visited[k] == 0 :
            dfs(k)




import sys
sys.stdin = open("길찾기.txt", "r")

t = 10
for tt in range(t):
    t_num, e = map(int,input().split())


    mat = [[] for _ in range(100)]
    list_ = list(map(int,input().split()))
    for i in range(0,len(list_),2):
        mat[list_[i]].append(list_[i+1])

    visited = [0 for _ in range(100)]

    dfs(0)
    if visited[99] :
        print("#{} 1".format(t_num))
    else:
        print("#{} 0".format(t_num))

