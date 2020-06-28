N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))


arr = sorted(arr, key=lambda x:(x[1],x[0] ))


cnt = 0
end = 0
for i in arr :
    ## end 보다 시작이 크면 겹칠 일이 없으니까
    if i[0] >= end :
        end = i[1]
        cnt += 1

print(cnt)