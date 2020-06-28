import sys

sys.stdin = open('금속막대.txt', 'r')


### 나사의 굵기는 수나사 x 암나사 굵기
### +은 연결
## 테스트 케이스 첫줄
## 막대의 개수 n개
### 수나사 암나사 2n 개
## 출력할 때는 연결 가장 길 수 할 수 있는 경우의 수

T = int(input())
for t in range(T):
    bolt = int(input())
    bolt_info = input().split()
    bolt_info = list(map(int,bolt_info))
    man_info = []
    wom_info = []
    f_list = [ ]



    for i in range( int(len(bolt_info)/2) ) :
        man_info.append(bolt_info[ (2*i)])
    for j in range( int(len(bolt_info)/2) ) :
        wom_info.append(bolt_info[(2*j) + 1])

    for k in range(len(man_info)):
        test = []
        test.append(man_info[k])
        test.append(wom_info[k])
        f_list.append(test)

    ## 가장 좌우는 포함을 안하니까 포함 안하는 것을 찾음
    ## 가장 첫 번째는 수나사
    #3 가장 마지막은 암나사

    ### 수나사로 가장 앞 찾기
    for a in range(len(man_info)) :
        if man_info[a] in wom_info :
            pass
        else :
            first = a

    for b in range(len(wom_info)) :
        if wom_info[b] in man_info :
            pass
        else :
            last = b

      ## first 는 초반 좌표 last는 마지막 좌표
    first_bolt = f_list[first]
    last_bolt = f_list[last]
    f_list.remove(f_list[first])
    man_info.remove(man_info[first])  ## 겹치니까 첫 번째 꺼 제거
    wom_info.remove(wom_info[first])


    result = [first_bolt[0], first_bolt[1]]  ## 첫 번째 나사 조합을 배치
    point = 1
    is_none = True



    while is_none :
        remove_m = man_info[man_info.index(result[point])]
        remove_w = wom_info[man_info.index(result[point])]

        result.append(man_info[man_info.index(result[point])])
        result.append(wom_info[man_info.index(result[point])])


        man_info.remove(remove_m)
        wom_info.remove(remove_w)
        point += 2
        if len(man_info) == 0:
            is_none = False
        else:
            pass

    result_text = ''
    for l in result :
        result_text += str(l) + ' '
    print(f'#{t+1} {result_text}')






















