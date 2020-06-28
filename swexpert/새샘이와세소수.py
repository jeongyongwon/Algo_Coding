import sys
sys.stdin = open('새샘이와세소수.txt','r')

T = int(input())
for t in range(1, T + 1):
    num = int(input())
    primitive = []
    for i in range(2, num):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            primitive.append(i)


    tt = []

    count = 0
    for k in range(len(primitive)):
        for l in range(k, len(primitive)):
            if (num - (primitive[k] + primitive[l])) >= primitive[l] and (
                    num - (primitive[k] + primitive[l])) in primitive:
                count += 1
    #             test = []
    #             test.append(primitive[k])
    #             test.append(primitive[l])
    #             test.append(num - (primitive[k] + primitive[l]))
    #             tt.append(test)
    # #
    print('#{} {}'.format(t, count))
    print(primitive)
