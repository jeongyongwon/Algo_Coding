import sys
sys.stdin = open('다솔이의다이아몬드장식.txt', 'r')

### '#'으로 이루어진 줄은 다섯줄이다

## 1,5 줄은  좌우 끝은 '..'으로 이뤄짐 / '#'의 개수는 글자수만큼이고 '#' 들 간의 사잉에는 3개의 '...'이다
## 2,4 번째 줄은 첫 번째 줄의 # 개수 2배이다 / . , #의 반복패턴이며 .으로 끝난다
### 3번째 줄은 글자 +1 의 #개수와 글자수 2배의 . 개수가 있고 / #으로 시작해서 . 글자. 패턴을 보인다


T = int(input())
for t in range(T) :
    text = input()
    line_1 = '' ; line_2 = '' ; line_3 = ''; line_4 = ''; line_5 = ''
    ##메인 3번 라인 처리
    for i in text :
        line_3 += f'#.{i}.'
    line_3 += '#'
    ## 길이확보
    leng = len(line_3)

    ## 2,4번 라인 처리
    for j in range(len(text)*2) :
        line_2 += '.#'
        line_4 += '.#'
    line_2 += '.' ; line_4 += '.'

    ### 1,5번 라인 처리
    line_1 += '..' ; line_5 += '..'
    for k in range(len(text) - 1):
        line_1 += '#...'
        line_5 += '#...'
    line_1 += '#..' ; line_5 += '#..'


    print(line_1)
    print(line_2)
    print(line_3)
    print(line_4)
    print(line_5)






