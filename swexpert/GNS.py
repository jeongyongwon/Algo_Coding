import sys
sys.stdin = open('GNS.txt', 'r')

T = int(input())
for t in range(T):
    t_num, num = input().split()
    num = int(num)
    list_ = list(input().split())

    code_ = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    cnt = []


    for i in range(len(code_)):
        cnt.append(list_.count(code_[i]))

    result = []
    for j in range(len(code_)) :
        for k in range(cnt[j]) :
            result.append(code_[j])


    print(t_num)
    print(' '.join(result))

