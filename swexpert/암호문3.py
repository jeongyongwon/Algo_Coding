import sys
sys.stdin = open('암호문3.txt', 'r')

### I  x, y, s  =>  insert(x) y개집어넣기, s는 y개의 숫자리스트
### D  x, y => x+1 위치부터 y개삭제 x,y = 4 이면 5,6,7,8의 인덱스를 제거
### A  y, s => 맨 뒤에 2개의 숫자르 붙임 s는 숫자들
### insert는 뒤로 밀림 집어넣으면
T = 10
for t in range(T) :
    leng = int(input())
    secret_ = list(map(int, input().split()))
    order_num = int(input())
    order_ = input().split()

    #### 조건마다 뒤에 조건 끌어쓰게 반복문 쓰면 됨 # extend([])집어넣
    for i in range(len(order_)) :
        if order_[i] == 'I' :
            for g in range( int(order_[i+2] )) :
                secret_.insert(int(order_[i+1])+1+g , int(order_[i+3+g]))

        elif order_[i] == 'D' :
            for j in range(int(order_[i+1])+1 , int(order_[i+1]) + int(order_[i+2]) + 1) :
                secret_.remove(secret_[j])


        elif order_[i] == 'A' :
            for k in range(  int(order_[i+1] )) :
                secret_.append(int(order_[i+k+2]))

        else :
            pass

    print( f'#{t+1}'," ".join(map(str, secret_[1:11])))






    



