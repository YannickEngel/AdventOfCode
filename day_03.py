from input_reader import read
import re
import numpy as np

input_lines = read.inputLines(3)
print(input_lines)

def parseInput(input):
    return [re.findall(r"(\d)", line) for line in input]

DATA = parseInput(input_lines)

#============================= Part One =============================


#============================= Part Two =============================