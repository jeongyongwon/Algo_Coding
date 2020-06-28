import sys
sys.stdin = open( '모음이보이지않는사람.txt' , 'r')

T = int(input())
for t in range(T):
    text_ = input()
    vowels = ['a','e','i','o','u']
    result = ''
    for i in range(len(text_)):
        if text_[i] not in vowels :
            result += text_[i]

    print(f'#{t+1} {result}')

