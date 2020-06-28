import sys
sys.stdin = open('파스칼의삼각형.txt', 'r')


T = int(input())
for t in range(T) :
    n = int(input())
    pascal = []
    start = [0, 1, 0]
    pascal.append(start)

    for i in range(9):
        pascal.append([0] * (i + 4))

    for j in range(1, len(pascal)):  ### 1에서 9 (10층)
        for k in range(len(pascal[j]) - 2):
            pascal[j][k + 1] += pascal[j - 1][k] + pascal[j - 1][k + 1]

    for a in range(len(pascal)) :
        pascal[a].remove(pascal[a][0]);  pascal[a].remove(pascal[a][-1])
    print(f'#{t+1}')

    for x in range(n):
        for y in range(len(pascal[x])):
            print(pascal[x][y], end=' ')
        print()






