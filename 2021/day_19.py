
import math
import re
import time

startTime = time.time()

input_lines = open(f"inputs/input_19.txt").read()

def parseInput(input):
    spl = input.split("\n")
    res = []
    temp = []
    for line in spl:
        if line == "":
            continue
        if line == "\n":
            continue
        if line[:2] == "--":
            if len(temp) != 0:
                res.append(temp)
                temp = []
        else:
            temp.append([(int(x),int(y),int(z)) for x,y,z in re.findall(r"(-?\d+),(-?\d+),(-?\d+)", line)][0])
    res.append(temp)
    return res

DATA = parseInput(input_lines)


foundPairs = []
relativPos1 = []
relativPos2 = []
fittedBeacons1Idx = []
fittedBeacons2Idx = []

signalData = [] #(pair, rotation, diff between 1 and 2)

found = False

startScanners = [DATA[0]]
endScanners = DATA[1:]
foundInRound = []

# take first scanner ---- scanner 1
    # for each beacon calc dists to other beacons
while len(startScanners) > 0:
    
    pair1 = startScanners.pop(0)
    foundInRound = []
    print("Using Scanner (1)", DATA.index(pair1))
    for pair2 in endScanners:
        print("Using Scanner (2)", DATA.index(pair2))
        found = False
        for bec in pair1:
            relativPos1 = []
            for beacon in pair1:
                relativPos1.append((bec[0] - beacon[0], bec[1] - beacon[1], bec[2] - beacon[2]))
        # for each scanner --- scnaner 2
            # for each beacon calc dist to other beacons
            for bec in pair2:
                relativPos2 = []
                for beacon in pair2:
                    relativPos2.append((bec[0] - beacon[0], bec[1] - beacon[1], bec[2] - beacon[2]))
                    #check for matches and note indexes of fitting distances incl. start beacon [0,0,0]
                count = 0
                for (x, y, z) in  (1,2,3), (1,3,-2), (1,-2,-3), (1,-3,2), (-2, 1, 3), (-2, 3, -1), (-2, -1, -3), (-2, -3, 1), (-1, -2, 3), (-1, 3, 2), (-1, 2, -3), (-1, -3, -2), (2, -1, 3), (2, 3, 1), (2, 1, -3), (2, -3, -1), (-3, 2, 1), (-3, 1, -2), (-3, -2, -1), (-3, -1, 2),(3, 2, -1), (3, -1, -2), (3, -2, 1), (3, 1, 2):
                    pos1 = abs(x) - 1
                    pos2 = abs(y) - 1 
                    pos3 = abs(z) - 1
                    pos1vz = 1 if x > 0 else -1
                    pos2vz = 1 if y > 0 else -1
                    pos3vz = 1 if z > 0 else -1
                    for i in range(1):
                        vz2 = 0
                        count = 0
                        fittedBeacons1Idx = []
                        fittedBeacons2Idx = []
                        for idx1 in range(len(relativPos1)):
                            for idx2 in range(len(relativPos2)):
                                if relativPos1[idx1][0] == pos1vz*relativPos2[idx2][pos1] and relativPos1[idx1][1] == pos2vz*relativPos2[idx2][pos2] and relativPos1[idx1][2] == pos3vz*relativPos2[idx2][pos3]:
                                    fittedBeacons1Idx.append(idx1)
                                    fittedBeacons2Idx.append(idx2)
                                    count += 1
                        if(len(fittedBeacons1Idx) >= 12):
                            found = True
                            startScanners.append(pair2)
                            foundInRound.append(pair2)
                            t1 = pair1[fittedBeacons1Idx[0]]
                            t2 = pair2[fittedBeacons2Idx[0]]
                            signalData.append(((DATA.index(pair1), DATA.index(pair2)), (x,y,z), (t1[0] - math.copysign(1, x) * t2[pos1], t1[1] - math.copysign(1, y) * t2[pos2],  t1[2] - math.copysign(1, z) * t2[pos3])))
                        if(found):
                            break
                    if(found):
                        break
                if(found):
                    break
            if(found):
                break
    for scan in foundInRound:
        endScanners.remove(scan)

for line in signalData:
    print(line)

queue = []
neighbours = []
rotTo0 = {
    0: (1,2,3)
    }
relTo0 = {
    0:(0,0,0)
    }
# start at 0
for date in signalData:
    if(date[0][0] == 0):
        queue.append(date)
        print(queue)

for date in queue:
    signalData.remove(date)
# go through each (0, x)


# calc rel position and rotations to 0 scanner 0
while len(queue) > 0:   
    neighbours = []
    q = queue.pop(0)
    x,y,z = rotTo0.get(q[0][0])

    rot = q[1]
    rotTo0[q[0][1]]= (int(rot[abs(x)-1]*math.copysign(1, x)), int(rot[abs(y)-1]*math.copysign(1, y)), int(rot[abs(z)-1]*math.copysign(1, z)))
    relPrevPos = relTo0.get(q[0][0])
    dist = q[2]
    relTo0[q[0][1]]= (int(relPrevPos[0] + dist[abs(x)-1]*math.copysign(1, x)), int(relPrevPos[1] + dist[abs(y)-1]*math.copysign(1, y)), int(relPrevPos[2] + dist[abs(z)-1]*math.copysign(1, z)))

    for date in signalData:
        if(date[0][0] == q[0][1]):
            neighbours.append(date)
    for ne in neighbours:
        queue.append(ne)
        signalData.remove(ne)

#
beacons = []
for beacon in DATA[0]:
    beacons.append(beacon)

for i in range (1,len(DATA)):
    relPos = relTo0.get(i)
    (x,y,z) = rotTo0.get(i)
    print(relPos)
    for beacon in DATA[i]:
        beacons.append((relPos[0] + beacon[abs(x)-1]*math.copysign(1, x), relPos[1] + beacon[abs(y)-1]*math.copysign(1, y), relPos[2] + beacon[abs(z)-1]*math.copysign(1, z)))

becs = [*set(beacons)]
print("Part 1: ", len(becs))

#===================================================================

distan = []
for t, b in relTo0.items():
    for s, b1 in relTo0.items():
        print
        distan.append(abs(b[0] - b1[0]) + abs(b[1] - b1[1]) + abs(b[2] - b1[2]))

print("Part 2: ", max(distan))

endTime = time.time()

print("Executinon Time (seconds): ", (endTime - startTime))