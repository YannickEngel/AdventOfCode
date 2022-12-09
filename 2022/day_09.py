import re

input = open(f"inputs/input_09.txt").read()

def updateKnots(posH1, posH2, posT1, posT2):
    if (abs(posH1 - posT1) > 1 or  abs(posH2 - posT2) > 1):
        if (posH1 == posT1):
            posT2 += 1 if posH2 > posT2 else -1
        elif (posH2 == posT2):
            posT1 += 1 if posH1 > posT1 else -1
        else:
            posT1 += 1 if posH1 > posT1 else -1
            posT2 += 1 if posH2 > posT2 else -1
    return posT1, posT2

moves = [(dir, int(count)) for dir, count in re.findall(r"(\w) (\d+)", input)]

#=================== Part 1 =================

hPos = [0,0]
tPos = [0,0]

visited = set()

for dir, count in moves:
    for _ in range(count):
        if (dir == 'U'):
            hPos[1] += 1
        elif(dir == 'D'):
            hPos[1] -= 1
        elif(dir == 'R'):
            hPos[0] += 1
        else: #L
            hPos[0] -= 1
        # update tail
        tPos[0], tPos[1] = updateKnots(hPos[0], hPos[1], tPos[0], tPos[1])

        posTup = (tPos[0], tPos[1])
        if posTup  not in visited:
            visited.add(posTup)

print("Part 1: ", len(visited))

#=================== Part 2 =================

visited = set()
hPos = [0,0]
knotPos = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]


for dir, count in moves:
    for _ in range(count):
        if (dir == 'U'):
            hPos[1] += 1
        elif(dir == 'D'):
            hPos[1] -= 1
        elif(dir == 'R'):
            hPos[0] += 1
        else: #L
            hPos[0] -= 1
        # update all tails
        knotPos[0][0], knotPos[0][1] = updateKnots(hPos[0], hPos[1], knotPos[0][0], knotPos[0][1])
        for i in range(1, len(knotPos)):
            knotPos[i][0], knotPos[i][1] = updateKnots(knotPos[i - 1][0], knotPos[i - 1][1], knotPos[i][0], knotPos[i][1])

        if (knotPos[8][0], knotPos[8][1]) not in visited:
            visited.add((knotPos[8][0], knotPos[8][1]))

print("Part 2: ", len(visited))