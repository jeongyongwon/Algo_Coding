import sys
sys.stdin = open('간단한369게임.txt', 'r')

n = int(input())
list_ = list(map(str,list(range(1,n+1))))
tac = ['3', '6', '9']


for i in range(len(list_)):
    line_ = ''
    for j in range(len(list_[i])):

        if list_[i][j] not in tac :
            pass
        else :
            if list_[i][j] == '3':
                line_ += '-'
            elif list_[i][j] == '6':
                line_ += '-'
            elif list_[i][j] == '9':
                line_ += '-'
            else :
                pass

    if '3' in list_[i] or '6' in list_[i] or '9' in list_[i] :
        list_[i] = line_
    else :
        pass
print(' '.join(list_))

