from input_reader import read
import re
import math

input_lines = read.inputLines(18)

def parseInput(input):
    return input

DATA = parseInput(input_lines)

#============================= Part One =============================

def explode(token):
    depth = 0
    for ind in range(len(token)):
        if depth >= 4 and token[ind] == '[' and token[ind + 3] == ']':
            #explode
            left, right = token[ind + 1], token[ind + 2]
            for i in range(1, ind -1):
                if isinstance(token[ind - i], int):
                    token[ind - i] += left
                    break
            for i in range(ind + 3, len(token) - 1):
                if isinstance(token[i], int):
                    token[i] += right
                    break
            token[ind: ind+4] = [0]
            return True
        if token[ind] == ']':
            depth -= 1
        if token[ind] == '[':
            depth += 1
    return False

def split(token):
    for ind in range(len(token)):
        if isinstance(token[ind], int) and token[ind] > 9:
            val = token[ind]
            token.insert(ind, '[')
            token.insert(ind + 1, int(math.floor(val/2)))
            token.insert(ind + 2, int(math.ceil(val/2)))
            token.insert(ind+3, ']')
            token.pop(ind+4)
            return True
    return False

def tokenize(expr):
    return [int(token) if '0' <= token[0] <= '9' else token
            for token in re.findall("\[|\]|\d+", expr)]

numbers = [tokenize(line.strip()) for line in DATA]

def reduce(token):
    while(explode(token) or split(token)):
        ...
    return token

def magnitude(token, index):
    currentTok = token[index]
    if token[index] == "[":
        val1 ,len1 = magnitude(token, index+1)
        index += len1
        val2, len2 = magnitude(token, index + 1)
        return 3*val1 + 2*val2, len1 + len2 + 1
    if isinstance(token[index], int):
        return token[index], 1
    if token[index] == "]":
        val, len =  magnitude(token, index +1)
        return val, len +1 

numbers_cpy = numbers.copy()
while(len(numbers) > 1):
    numbers[0] = reduce(['['] + numbers[0] + numbers[1] + [']'])
    numbers.pop(1)



print(f"Result Part 1: {magnitude(numbers[0], 0)[0]}")

#============================= Part Two =============================


maxMag = 0
for i in range(len(numbers_cpy)):
    for j in range(len(numbers_cpy)):
        if(i != j):
            res, _ = magnitude(reduce(['['] + numbers_cpy[i] + numbers_cpy[j] + [']']),0)
            maxMag = max(maxMag, res)
print(f"Result Part 2: {maxMag}")