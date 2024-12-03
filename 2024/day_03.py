import re
from functools import reduce

DATA = open(f"inputs/input_03.txt").read()

def interpret_muls(input):
    sum = 0
    instr = list(map(lambda x: re.findall(r'\d+', x),re.findall(r'mul\(\d+,\d+\)', input)))
    sum = reduce(lambda l,r : (l + int(r[0])*int(r[1])), instr, 0)
    return sum
    

def interpret(input):
    sum = 0
    instr = list(map(lambda x: (list(map(lambda y: int(y),re.findall(r'\d+', x)))) if (x != "do()" and x != "don't()") else x ,re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', input)))
    enabled = 1
    for inst in instr:
        if len(inst) == 2:
            sum += inst[0] * inst[1] * enabled
        else: 
            enabled = 1 if inst == "do()" else 0
    return sum


#for x,y in list(map(lambda x: re.findall(r'\d+', x),muls)):
    #sum += int(x)*int(y)

print("Part 1: ", interpret_muls(DATA))
print("Part 2: ", interpret(DATA))