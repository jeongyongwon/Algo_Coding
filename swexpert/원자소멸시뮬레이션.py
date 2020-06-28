import sys
sys.stdin = open('원자소멸.txt','r')

for t in range(1,int(input())+1):
    N = int(input())

    ### x, y, 이동방향 (이동방향 바뀌지않은) , 에너지지