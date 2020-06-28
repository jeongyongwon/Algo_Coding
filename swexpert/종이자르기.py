w, h = map(int,input().split())
mat = []
for i in range(h+1):
    mat.append([0]*(w+1))
slice_ = int(input())
## 0은 가로로 자르고 1은 세로로 자르고

for i in range(slice_):
    direct, point = map(int,input().split())
    if direct == 0 :
        for k in range(len(mat[point])):
            mat[point][k] = 1
    else :
        for j in range(len(mat)):
            mat[j][point] = 1

rcut_list = []
ccut_list = []

for i in range(len(mat[0])):
    if mat[0][i] == 1:
        ccut_list.append(i)

for j in range(len(mat)) :
    if mat[j][0] == 1 :
        rcut_list.append(j)

c_list = []
r_list = []


r_list.append(rcut_list[0]) ##첫 번째 행
c_list.append(ccut_list[0]) ##첫 번째 열




for i in range(len(rcut_list)-1):
    r_list.append(rcut_list[i+1] - rcut_list[i])

for j in range(len(ccut_list)-1):
    c_list.append(ccut_list[j+1] -ccut_list[j])

r_list.append(h-rcut_list[-1])
c_list.append(w-ccut_list[-1])

resol = 0
for i in r_list :
    for j in c_list :
        if  i*j > resol :
            resol = i*j
        else :
            pass
print(resol)
print('-----------')
print(r_list,c_list)

for kk in range(len(mat)):
    print(mat[kk])












