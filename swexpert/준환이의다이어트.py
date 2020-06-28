import sys
sys.stdin = open('준환이의다이어트.txt', 'r')


T = int(input())
for t in range(T) :
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if c < a :
        print(f'#{t+1} {a-c}')
    elif a < c < b :
        print(f'#{t+1} {0}')
    else :
        print(f'#{t+1} {-1}')