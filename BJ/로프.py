N = int(input())

line = []

for i in range(N):
    line.append(int(input()))


line = sorted(line, reverse=True)

## max
res = line[0]

i = 1
cut = 2
is_end = True

if len(line) == 1:
    pass

else :
    while is_end :
        if i == len(line):
            is_end = False
            break

        prove = cut * line[i]

        if res < prove :
            res = prove

        else :
            is_end = False
            break

        cut += 1
        i += 1

print(res)







