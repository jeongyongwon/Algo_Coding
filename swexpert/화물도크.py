# def comb(idx,cnt,N,arr,selected):
#     global prove, res, can
#     if can == True:
#         return
#
#     if cnt == N :
#         test = []
#         for i in range(len(arr)):
#             if selected[i] == 0:
#                 test.append(i)
#
#         for i in test:
#             for j in range(arr[i][0] ,arr[i][1]):
#                 time[j] -= 1
#
#         pve = 0
#
#         for i in range(len(time)):
#             if time[i] > 1:
#                 pve += 1
#                 break
#
#         if pve > 0:
#             for i in test:
#                 for j in range(arr[i][0], arr[i][1]):
#                     time[j] += 1
#             return
#
#         else :
#             can = True
#             return
#
#
#     if idx == len(arr):
#         return
#
#     selected[idx] = 1
#     comb(idx+1,cnt+1,N,arr,selected)
#     if can == True:
#         return
#     selected[idx] = 0
#     comb(idx+1,cnt,N,arr,selected)
#     if can == True:
#         return
#
#

import sys
sys.stdin = open('화물도크.txt','r')

T = int(input())
for t in range(1, 1+T):
    N = int(input())
    time = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x: (x[1], x[0]))
    print(time)
    end = 0
    cnt = 0
    for i in time:
        if i[0] >= end:
            end = i[1]
            cnt += 1
    print('#{} {}'.format(t, cnt))









