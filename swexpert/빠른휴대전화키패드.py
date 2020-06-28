import sys
sys.stdin = open('빠른휴대전화키패드.txt','r')

for t in range(1,int(input())+1):
    S, N = map(int,input().split())
    S = str(S)

    texts = list(input().split())




    typing = {'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3','g':'4','h':'4','i':'4','j':'5','k':'5','l':'5','m':'6','n':'6','o':'6'
        ,'p':'7','q':'7','r':'7','s':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9',}


    cnt = 0

    for text in texts:
        prove = ''
        for i in text:
            prove += typing[i]
        if S == prove :
            cnt += 1


    print(f'#{t} {cnt}')