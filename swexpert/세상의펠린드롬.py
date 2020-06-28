import sys
sys.stdin = open('세상의펠린드롬.txt','r')

for t in range(1,int(input())+1 ):
    text = list(input())
    re_text = list(reversed(text))


    if '?' not in text:
        if text == re_text:
            print(f'#{t} Exist')
        else:
            print(f'#{t} No exist')
    else:
        for i in range(len(re_text)):
            if re_text[i] == '?':
                re_text[i] = text[i]
                text[len(text)-1-i] = re_text[len(text)-1-i]

        if text == re_text:
            print(f'#{t} Exist')
        else:
            print(f'#{t} No exist')





