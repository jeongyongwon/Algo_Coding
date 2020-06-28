import sys
sys.stdin = open('가장빠른문자열타이핑.txt','r')
# for t in range(1,int(input())+1):
#     A,B = input().split()
#
#     cnt = 0
#
#     i = 0
#     k = 0
#     stop = 0
#     is_end = True
#     while is_end:
#         if i >= len(A):
#             is_end = False
#             break
#         else :
#             if A[i] == B[0]:
#                 if A[i:i+len(B)] == B:
#                     i += len(B)
#                     cnt +=1
#             else :
#                 i += 1
#                 cnt += 1
#
#     print(f'#{t} {cnt}')
T = int(input())
for tc in range(1, T+1):
    word = input().split()
    ans = word[0].count(word[1])
    word[0]=word[0].replace(word[1],"")
    print("#{} {}".format(tc, ans+len(word[0])))