import sys

sys.stdin = open('농작물수확하기.txt', 'r')

T = int(input())
for t in range(T):
    n = int(input())
    mat = []
    for nn in range(n):
        mat.append(list(map(int, input())))

    center = int(n/2)
    result = 0
    is_end = True
    i = 0


    while is_end :
        if len(mat) > 1:
            result += sum(mat[0 + i][center - i:center + i + 1])
            result += sum(mat[len(mat) - 1 - i][center - i:center + i + 1])

            i += 1
            if 2 * i + 1 >= len(mat):
                is_end = False
        else :
            result += mat[0][0]



    result += sum(mat[center][:])


    print(f'#{t+1} {result}')