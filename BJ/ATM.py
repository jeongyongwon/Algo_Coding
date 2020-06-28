N = int(input())
arr = sorted(list(map(int,input().split())))

res = 0
i = 0
while arr :
    res += len(arr) * arr[i]
    arr.pop(0)

print(res)