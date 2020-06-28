import sys
sys.stdin = open('베이비진게임.txt','r')

for t in range(1,int(input())+1):
    arr = list(input().split())

    ##무승부
    card_1 = {}
    card_2 = {}
    result = 0

    for i in range(10):
        card_1[str(i)] = 0
        card_2[str(i)] = 0


    is_end = True
    turn = 0


    while is_end :
        if turn >= len(arr):
            is_end = False
            break

        elif turn <= 3:
            if turn % 2 == 0:
                card_1[arr[turn]] += 1

            else :
                card_2[arr[turn]] += 1


        else :
            if turn % 2 == 0:
                card_1[arr[turn]] += 1
                for i in range(7):
                    if card_1[str(i)] > 0 and  card_1[str(i+1)] > 0 and card_1[str(i+2)] > 0 :
                        result = 1
                        is_end = False
                        break

                for i in range(len(card_1)):
                    if card_1[str(i)] >= 3:
                        result = 1
                        is_end = False
                        break

            else :
                card_2[arr[turn]] += 1
                for i in range(7):
                    if card_2[str(i)] > 0 and card_2[str(i+1)] > 0 and card_2[str(i+2)] :
                        result = 2
                        is_end = False
                        break

                for i in range(len(card_2)):
                    if card_2[str(i)] >= 3 :
                        result = 2
                        is_end = False
                        break

        turn += 1


    print(f'#{t} {result}')









