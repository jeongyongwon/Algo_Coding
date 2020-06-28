import sys
sys.stdin = open('반복문자.txt', 'r')

t = int(input())
for tt in range(t):
    text = list(input())


    i = 0
    is_end = True
    while is_end :
        if i >= len(text) - 1:
            is_end = False
        else :
            if text[i] == text[i+1]:
                del text[i:i+2]
                i = 0
            else :
                i += 1

    print(f'#{tt+1} {len(text)}')