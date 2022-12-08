import re
import numpy as np
import math

input_lines = open(f"inputs/input_03.txt").read()

def parseInput(input):
    return [res for res in re.findall(r"(\d+)", input)]

DATA = parseInput(input_lines)

#============================= Part One =============================
gamma_rate = ""
eps_rate = ""
for i in range(len(DATA[0])):
    col = np.array([line[i] for line in DATA])
    if(np.count_nonzero(col == "1") >= int(math.ceil(len(col)/2))):
        gamma_rate += "1"
        eps_rate += "0"
    else:
        gamma_rate += "0"
        eps_rate += "1"

print(f"Result Part 1: {int(gamma_rate, 2) * int(eps_rate, 2)}")
#============================= Part Two =============================

inp1 = DATA.copy()
inp2 = DATA.copy()

for i in range(len(inp1[0])):
    if(len(inp1) == 1):
        break
    col = np.array([line[i] for line in inp1])
    most = "1" if(np.count_nonzero(col == "1") >= int(math.ceil(len(col)/2))) else "0"
    new = []
    for line in inp1:
        if line[i] == most:
            new.append(line)
    inp1 = new


for i in range(len(inp2[0])):
    if(len(inp2) == 1):
        break
    col = np.array([line[i] for line in inp2])
    most = "1" if(np.count_nonzero(col == "1") < int(math.ceil(len(col)/2))) else "0"
    new = []
    for line in inp2:
        if line[i] == most:
            new.append(line)
    inp2 = new

print(f"Result Part 2: {int(inp1[0], 2) * int(inp2[0], 2)} ")
