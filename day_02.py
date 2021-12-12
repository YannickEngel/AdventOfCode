from input_reader import read
import re

input_lines = read.input(2)

def parseInput(input):
    return [(direction, int(amount)) for direction, amount in re.findall(r"(\w+) (\d+)", input)]

DATA = parseInput(input_lines)

#============================= Part One =============================

horizontal = vertical = 0
for dir, amount in DATA:
    if(dir == "forward"):
        horizontal += amount
    elif(dir == "down"):
        vertical += amount
    elif(dir == "up"):
        vertical -= amount

print(vertical * horizontal)
#============================= Part Two =============================

horizontal = vertical = aim = 0
for dir, amount in DATA:
    if(dir == "forward"):
        horizontal += amount
        vertical += aim * amount
    elif(dir == "down"):
        aim += amount
    elif(dir == "up"):
        aim -= amount
print(vertical * horizontal)
