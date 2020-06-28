import sys
sys.stdin = open('숫자를정렬하자.txt','r')
t = int(input())
for tt in range(t):
    leng = int(input())
    num_ = list(map(int,input().split()))


    num_ = list(map(str,sorted(num_)))
    print(f'#{tt+1}',' '.join(num_))


