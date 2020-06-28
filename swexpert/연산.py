


import sys
import collections
sys.stdin = open('연산.txt','r')

for t in range(1,int(input())+1):
    start, end = map(int,input().split())

    cal = [1,1,2,10]
    # + - * -

    result = 0
    deq = collections.deque([[start,0]])
    is_end = True
    visit = [0] * 1000001

    while is_end :

        num, stage  = deq.popleft()
        if num > 1000000 or num <= 0:
            pass
        else :

            if num == end :
                is_end = False
                result = stage
                break
            else:
                stage += 1

                for i in range(4):

                    if i == 0 :
                        try:
                            if num+1 <= 1000000 :
                                if visit[num+1] == 0 :
                                    visit[num+1] = 1
                                    deq.append([num+1, stage])
                                else:
                                    pass
                            else :
                                pass
                        except KeyError:
                            if num+1 <= 1000000:
                                visit[num+1] = stage
                                deq.append([num+1, stage ])
                            else :
                                pass


                    elif i == 1 :
                        try:
                            if num-1 > 0:
                                if visit[num-1] == 0 :
                                    visit[num-1] = 1
                                    deq.append([num-1, stage ])
                                else:
                                    pass
                            else :
                                pass
                        except KeyError:
                            if num-1 > 0:
                                visit[num-1] = stage
                                deq.append([num-1, stage ])
                            else :
                                pass


                    elif i == 2 :
                        try:
                            if num*2 <= 1000000 :
                                if visit[num*2] == 0 :
                                    visit[num*2] = 1
                                    deq.append([num*2, stage ])
                                else:
                                    pass
                            else :
                                pass
                        except KeyError:
                            if num*2 <= 1000000 :
                                visit[num*2] = stage
                                deq.append([num*2, stage ])
                            else :
                                pass


                    else :
                        try:
                            if num-10 > 0:
                                if visit[num-10] == 0 :
                                    visit[num-10] = 1
                                    deq.append([num-10, stage])
                                else:
                                    pass
                            else :
                                pass
                        except KeyError:
                            if num-10:
                                visit[num-10] = stage
                                deq.append([num-10, stage ])
                            else :
                                pass

    print(f'#{t} {result}')
