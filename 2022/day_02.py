import re

input = open(f"inputs/input_02.txt").read()
DATA = [(play, response) for play, response in re.findall(r"(\w) (\w)", input)]

valueAct = {
    "A": 0,
    "B": 1,
    "C": 2
}

valueResp = {
    "X": 0,
    "Y": 1,
    "Z": 2
}

wantedOutcome = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

outcome = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

#=============================================================== 
# first version

sum_1 = 0
sum_2 = 0

for (action, response) in DATA:
    sum_1 += valueResp.get(response) + 1 + outcome[valueAct.get(action)][ valueResp.get(response)]
    sum_2 += outcome[valueAct.get(action)].index(wantedOutcome.get(response)) + wantedOutcome.get(response) + 1

print("Part 1: ", sum_1)
print("Part 2: ", sum_2)

#==============================================================
# second version (no use of dictonaries)

sum_1 = 0
sum_2 = 0

for (action, response) in DATA:
    responseVal = ord(response) - ord("X")
    actionVal = ord(action) - ord("A")
    sum_1 += responseVal + outcome[actionVal][responseVal] + 1    
    sum_2 += outcome[actionVal].index(responseVal * 3) + (responseVal * 3) + 1


print("Part 1: ", sum_1)
print("Part 2: ", sum_2)