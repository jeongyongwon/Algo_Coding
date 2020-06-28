import sys
sys.stdin = open('이진수.txt','r')
for t in range(1,int(input())+1):
    N, num_16 = input().split()
    num_10 = int(num_16, 16)
    binary = bin(num_10)
    modify = '0' * (int(N) * 4 - len(binary[2:]))
    print(f"#{t} {modify + binary[2:]}")

