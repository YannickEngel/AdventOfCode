import numpy as np

input_lines = open(f"inputs/input_01.txt").read()

def parseInput(input):
    return [sum(map(int, line.split())) for line in input.split("\n\n")]

DATA = parseInput(input_lines)
#============================= Part One =============================
max = max(DATA)
print("Part 1: ", max)

#============================= Part Two =============================

maxElves = np.sort(DATA)
print("Part 2: ", np.sum(maxElves[-3:])) 