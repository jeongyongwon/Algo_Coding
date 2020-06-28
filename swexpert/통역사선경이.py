import sys
sys.stdin  = open('통역사선경이.txt', 'r')

T = int(input())
for t in range(T):
    leng = int(input())
    text_ = input()
    goodoo = ['.','?','!',' ']
    num = [1,2,3,4,5,6,7,8,9,0]
    num = list(map(str,num))

    i = 0
    is_end = True
    test_ = ''
    t_list = []
    for i in text_ :
        if i not in goodoo :
            test_ += i
        else :
            t_list.append(test_)
            t_list.append(i)
            test_ = ''


    up_list = []
    for i in range(len(t_list)):
        if t_list[i] == ' ' or t_list[i] == '':
            pass

        elif not t_list[i][0].islower()  :
            up_list.append(t_list[i])

    cnt = 0
    cnt_list = []
    for i in range(len(up_list)):
        if up_list[i] == '!' or up_list[i] == '?' or up_list[i] == '.':
            cnt_list.append(cnt)
            cnt = 0
        else :
            pro_cnt = 0
            for j in range(len(up_list[i])):
                if up_list[i][j] in num :
                    pro_cnt += 1
            for j in range(len(up_list[i]) - 1 ):
                if up_list[i][j+1].isupper():
                    pro_cnt += 1

            if pro_cnt == 0 :
                cnt += 1
            pro_cnt = 0


    cnt_list = list(map(str,cnt_list))
    print('#{}'.format(t+1),' '.join(cnt_list) )












