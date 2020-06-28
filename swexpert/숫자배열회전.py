import sys
sys.stdin = open('숫자배열회전.txt','r')
t = int(input())
for tt in range(t):
    n = int(input())

    mat = []
    for i in range(n):
        mat.append(list(input().split()))

    result =[[] for _ in range(n)]

    ## 90도 부터


    for i in range(n):
        for j in range(n):
            result[i] += mat[j][i]
        result[i].reverse()


    ## 180도 부터

    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            result[len(result)-i-1] += mat[i][j]

    ### 270도 부터
    for j in range(n-1,-1,-1):
        for i in range(n):
            result[len(result)-j-1]  += mat[i][j]

    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i] =''.join(result[i])

    print('#{}'.format(tt+1))
    for i in range(len(result)):
        for j in range(0,len(result[0]),n):
            print(result[i][j:j+n], end = ' ' )
        print()