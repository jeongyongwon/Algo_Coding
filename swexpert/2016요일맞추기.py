import sys
sys.stdin = open('요일맞추기.txt','r')
month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

month_day = [0]
days = [0,1,2,3,4,5,6]
for i in month.values():
    month_day.append(i)



for t in range(int(input())):
    m, d = map(int,input().split())

    day = 0
    if m == 1 :
        day += month_day[0] + d
    else :
        day += sum(month_day[0:m]) + d

    result = 0

    if day % 7 == 0:
        result = 3
    if day % 7 == 1:
        result = 4
    if day % 7 == 2:
        result = 5
    if day % 7 == 3:
        result = 6
    if day % 7 == 4:
        result = 0
    if day % 7 == 5:
        result = 1
    if day % 7 == 6:
        result = 2

    print(f'#{t+1} {result}')