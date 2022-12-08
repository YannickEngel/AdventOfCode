import numpy as np
import re

input_lines = open(f"inputs/input_01.txt").read()

def parseInput(input):
    return np.array(list(map(int, re.findall(r"(\d+)", input))))

DATA = parseInput(input_lines)

#============================= Part One =============================
count = 0
for i in range(1,DATA.size):
    if DATA[i] > DATA[i-1]:
        count +=1
print(count)

#============================= Part Two =============================
def get3sum(index):
    return DATA[index] + DATA[index+ 1] + DATA[index+ 2]
count = 0
for i in range(1,DATA.size - 2):
    if get3sum(i) > get3sum(i-1):
        count +=1
print(count)