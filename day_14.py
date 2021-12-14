from input_reader import read
import re
from collections import Counter

input_lines = read.input(14)

def parseInput(input):
    polyTemp, rules = input.split('\n\n')
    seperateRules = {pairs: insertion for pairs, insertion in re.findall(r"(\w+) -> (\w)", rules)}
    return polyTemp, seperateRules

START_POLY, RULES = parseInput(input_lines)

#============================= Part One =============================


def doStep(poly, rules):
    new_poly = ""
    for i in range(len(poly) -1):
        insert = rules[poly[i: i+2]]
        new_poly += (poly[i]+insert)
    new_poly += poly[len(poly) -1]
    return new_poly

poly = START_POLY
for i in range(10):
    poly = doStep(poly, RULES)

coll = Counter(poly)
max = 0
min = coll['B']
for key in coll.keys():
    if coll[key] > max:
        max = coll[key]
    elif coll[key] < min:
        min = coll[key]
#print(f"max: {max}, min: {min}")
print(f"Result Part 1: {max - min}")
#============================= Part Two =============================

#changed version of doStep for part2 to handle higher amounts of steps
def doStep2(counter, rules):
    count = Counter()
    for fst, snd in counter:
        middle = rules[fst+snd]
        count[fst+middle] += counter[fst+snd]
        count[middle+snd] += counter[fst+snd]
    return count

counter = Counter([START_POLY[i:i+2] for i in range(len(START_POLY)-1)])
for i in range(40):
    counter = doStep2(counter, RULES)

chrCount = Counter()
for fst,snd in counter:
    chrCount[fst] += counter[fst+snd]
chrCount[START_POLY[-1]] += 1 #last element is missed by for loop

min = chrCount[list(chrCount.keys())[0]]
for key in chrCount.keys():
    if chrCount[key] > max:
        max = chrCount[key]
    elif chrCount[key] < min:
        min = chrCount[key]
#print(f"max: {max}, min: {min}")
print(f"Result Part 2: {max - min}")