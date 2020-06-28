

R,C,D = map(int,input().split())

mat = []
for i in range(R):
    mat.append(list(map(int,input().split())))


### 궁수들이 서 있을 수  있는 방법은 5c3

print(permute([1,2,3,4]))
