input =  open(f"input_reader/inputs/input_08.txt").readlines()

DATA = []

for i in range(len(input)):
    DATA.append([])
    for ch in input[i]:
        DATA[i].append(ch)

sum = 0

for i in range(len(DATA)):
    for j in range(len(DATA[i])):
        if i == 0 or j == 0 or i == len(DATA) - 1 or j == len(DATA[i]) - 1:
            sum += 1
            continue
        visX1 = True
        visX2 = True
        visY1 = True
        visY2 = True
        maxH = DATA[i][j]

        for x in range(i):
            if (DATA[i-x-1][j] >= maxH):
                visX1 = False
                break
        for x in range(len(DATA) - i  - 1):
            if (DATA[i + x + 1][j] >= maxH):
                visX2 = False
                break
        for y in range(j):
            if (DATA[i][j-y - 1] >= maxH):
                visY1 = False
                break
        for y in range(len(DATA[i]) - j - 1):
            if (DATA[i][j + y + 1] >= maxH):
                visY2 = False
                break
        if (visX1 or visX2 or visY1 or visY2):
            sum += 1

def scen(i,j):
    maxH = DATA[i][j]
    up = 0
    for x in range(i):
        up += 1
        if (DATA[i-x-1][j] >= maxH):
            break
    down = 0
    for x in range(len(DATA) - i  - 1):
        down += 1
        if (DATA[i + x + 1][j] >= maxH):
            break
    left = 0
    for y in range(j):
        left += 1
        if (DATA[i][j-y - 1] >= maxH):
            break
    right = 0
    for y in range(len(DATA[i]) - j - 1):
        right += 1
        if (DATA[i][j + y + 1] >= maxH):
            break
    return up * down * left * right

print("Part 1", sum)

score = 0
for i in range(len(DATA)):
    for j in range(len(DATA[0])):
        score = max(score, scen(i,j))

print("Part 2 ", score)