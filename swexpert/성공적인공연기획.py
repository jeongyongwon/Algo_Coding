import sys
sys.stdin = open('성공적인공연기.txt', 'r')
for t in range(int(input())):
    people = list(map(int,input().split()))
    