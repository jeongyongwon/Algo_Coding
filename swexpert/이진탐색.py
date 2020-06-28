import sys
sys.stdin = open('이진탐색.txt','r')

for t in range(1,int(input())+1):
    A, B = map(int,input().split())

    arr_a = list(map(int,input().split()))
    arr_b = list(map(int,input().split()))


    res = 0


    while len(arr_b):

        num = arr_b.pop(0)
        is_end = True


        start = 0
        end = len(arr_a)-1

        while start <= end :
            mid = (start + end) // 2
            if num == arr_a[mid]:
                res += 1
                break

            elif num > arr_a[mid] :
                start = mid + 1
            else :
                end = mid - 1


    print(f'#{t} {res}')