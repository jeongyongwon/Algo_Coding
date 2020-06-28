import sys

sys.stdin = open("input.txt", "r")
T = 10
for t in range(1,T+1):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    # (한 줄입력받아서, 띄어쓰기 구분하고, 숫자변경, 리스트로 변경) *100
    # 가장 짧은 거리를 저장하는 변수,
    min_path = 10000
    # 가장 짧은 거리를 순회하는 시작점 저장하는 변수
    min_position = 0
    #시작점 설정하기
    for i in range(100):
        row = 0
        # 만약에 사다리 시작점이면, 시작
        if ladder[row][i] == 1:
            # 시작
            direct = 1     # 1: 아래   2: 오른   3: 왼
            col = i     # 시작 열 설정
            count = 0
            # 진행방향 확인하고, 다음 갈 곳을 정의, 맨마지막줄 도착할 때 까지
            while row < 100:
                # 이동
                if direct == 1: #  아래 방향
                    # 오른쪽 한 번 확인하고, 왼쪽 확인
                    # 오른쪽이나 왼쪽중 갈 곳있으면 방향 전환
                    if col + 1 < 100 and ladder[row][col+1] == 1:
                        direct = 2
                        col += 1
                    elif col - 1 >= 0 and ladder[row][col-1] == 1:
                        direct = 3
                        col -= 1
                    else:   # 오른쪽 왼쪽 둘다 갈길이 없으면, 아래로
                        row += 1
                elif direct == 2:   # 오른 방향
                    # 아래쪽으로 내려가는 길이 있으면,
                    if ladder[row+1][col] == 1:
                        direct = 1  # 방향전환
                        row += 1    # 아래쪽으로 위치 전환
                    else:
                        col += 1
                elif direct == 3:   # 왼 방향
                    if ladder[row+1][col] == 1:
                        direct = 1
                        row += 1
                    else:
                        col -= 1
                count += 1
                if count > min_path:    # 제일 짧은 경로만 있으면 됨
                    break

            if count <= min_path:
                # 이동 횟수가 적으면, 이동횟수와, 시작점을 저장
                min_path = count
                min_position = i

    print("#%d" % t, min_position)
