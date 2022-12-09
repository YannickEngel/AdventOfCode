import re
import copy

input = open(f"inputs/input_05.txt").read()

#create start stack
data_stacks = input.split("\n\n")[0].split("\n")
start = [[], [], [], [], [], [], [], [], []]

for line in data_stacks[:-1]:
    for i in range(9):
        if(line[1 + i*4] != " "):
            start[i].append(line[1 + i*4])
#reverse stacks
for i in range(len(start)):
    start[i] = start[i][::-1]

DATA = re.findall(r"(\d+) from (\d+) to (\d+)", input.split("\n\n")[1]) # move 4 from 9 to 6

# =========================== Part 1 ================================

stacks = copy.deepcopy(start)
for (amount, fro, to) in DATA:
    for i in range(int(amount)):
        stacks[int(to) - 1].append(stacks[int(fro) - 1].pop())

print("Part 1: ", "".join([stack[-1] for stack in stacks]))

# =========================== Part 2 ================================

stacks = copy.deepcopy(start)
for (amount, fro, to) in DATA:
    stacks[int(to) - 1].extend(stacks[int(fro)-1][-int(amount):])
    stacks[int(fro) - 1] = stacks[int(fro) - 1][:-int(amount)]

print("Part 2: ", "".join([stack[-1] for stack in stacks]))
