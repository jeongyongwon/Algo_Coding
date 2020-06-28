import sys
sys.stdin = open('영준이의카드카운팅.txt', 'r')


T = int(input())
for t in range(T) :
    info =  list(input())

    s_num = 0
    s_dict = {}
    d_num = 0
    d_dict = {}
    h_num = 0
    h_dict = {}
    c_num = 0
    c_dict = {}


    for i in range( int(len(info)/3)):
        if info[3 * i] == 'S' :
            if info[(3*i) + 1] + info[(3*i) + 2] not in s_dict:
                s_dict[ info[ (3 * i) + 1 ] + info[(3 * i) + 2] ] = 1
            else :
                s_dict[info[(3 * i) + 1] + info[(3 * i) + 2]]  += 1
        elif info[3 * i] == 'D':
            if info[(3*i) + 1] + info[(3*i) + 2] not in d_dict :
                d_dict[info[(3*i) + 1] + info[(3*i) + 2]] = 1
            else :
                d_dict[info[(3 * i) + 1] + info[(3 * i) + 2]] += 1
        elif info[3*i] == 'H':
            if info[(3*i) + 1] + info[(3*i) + 2] not in h_dict :
                h_dict[info[(3*i) + 1] + info[(3*i) + 2]] = 1
            else :
                h_dict[info[(3 * i) + 1] + info[(3 * i) + 2]] += 1
        elif info[3*i] == 'C' :
            if info[(3*i)+1] + info[(3*i)+2] not in c_dict:
                c_dict[info[(3*i)+1] + info[(3*i)+2]] = 1
            else :
                c_dict[info[(3 * i) + 1] + info[(3 * i) + 2]] += 1
        else :
            pass


    if 2 in list(s_dict.values()) or 2 in list(d_dict.values()) or 2 in list(h_dict.values()) or 2 in list(c_dict.values()) :
        print(f'#{t+1} ERROR')
    else :
        print(f'#{t+1} {13- sum(list(s_dict.values())) } {13- sum(list(d_dict.values())) } {13- sum(list(h_dict.values())) } {13- sum(list(c_dict.values())) }')






















