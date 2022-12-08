import statistics
import math

input_lines = open(f"inputs/input_07.txt").read()

def parseInput(input):
    return list(map(int, input.split(',')))

DATA = parseInput(input_lines)

#============================= Part One =============================



def calFuel(arr, pos):
    fuel = 0
    for i in arr:
        fuel += abs(i - pos)
    return fuel

min = min(DATA)
max = max(DATA)

position = statistics.median(DATA)
print(f"Result Part 1: {calFuel(DATA,int(position))}")


#============================= Part Two =============================
def calFuelInc(arr, pos):
    fuel = 0
    for val in arr:
        fuel += sum(list(range(1,abs(val-pos)+1)))
    return fuel

position = statistics.mean(DATA)
fuel1 = calFuelInc(DATA, int(math.ceil(position)))
fuel2 = calFuelInc(DATA, int(math.floor(position)))
if (fuel1 < fuel2):
    print(f"Result Part 2: {fuel1}")
else:
    print(f"Result Part 2: {fuel2}")

