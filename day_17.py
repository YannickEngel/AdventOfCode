from input_reader import read
import re
import math

input_lines = read.input(17)
print(input_lines)

def parseInput(input):
    return ((re.findall(r"x=(\d+)..(\d+)", input)[0]), (re.findall(r"y=(-\d+)..(-\d+)", input)[0]))

DATA = parseInput(input_lines)
x_min = int(DATA[0][0])
x_max = int(DATA[0][1])
y_min = int(DATA[1][0])
y_max = int(DATA[1][1])
#============================= Part One =============================

def landsInTarget(xv, yv):
    x = y = y_peak = 0
    x += xv
    y += yv
    while(x <= x_max and y >= y_min):
        y_peak = max(y, y_peak)
    
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True, y_peak
        if xv > 0:
            xv -= 1
        elif xv <0:
            xv += 1
        yv -= 1
        x += xv
        y += yv
    return False, 0

maxy = 0
count = 0
for vx in range(0,x_max+1):
    for vy in range(y_min, -y_min): 
        lands, val = landsInTarget(vx, vy)
        if lands and val > -math.inf:
            count += 1
            maxy = max(maxy, val)

print(f"Result Part 1: {maxy}")
print(f"Result Part 2: {count}")