

input_lines = open(f"inputs/input_06.txt").read()
def parseInput(input):
    return[input.count(str(i)) for i in range(9)]

DATA = parseInput(input_lines)

#============================= Part One =============================
def cycle(days, ages):
    for _ in range(days):
        new = ages[0]
        for i in range(len(ages) - 1):
            ages[i] = ages[i + 1]
        ages[6] += new
        ages[8] = new
    return sum(ages)

print(cycle(80, DATA.copy()))
#============================= Part Two =============================

print(cycle(256, DATA.copy()))