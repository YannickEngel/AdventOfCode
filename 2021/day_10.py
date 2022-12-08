input_lines = open(f"inputs/input_10.txt").read()

def parseInput(input):
    return input

DATA = parseInput(input_lines)

charsToPoints1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

charsToPoints2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

#============================= Part One =============================
def isClosingTo(opening, closing):
    if opening == "(":
        return closing == ")"
    elif opening == "[":
        return closing == "]"
    elif opening == "{":
        return closing == "}"
    elif opening == "<":
        return closing == ">"
    else:
        return False

def isCorrect(line):
    stack = []
    fault_char = ""
    for char in line:
        if char in "([{<":
            stack.append(char)
        else:
            if stack == []:
                break
            elif isClosingTo(stack[-1], char):
                stack.pop()
            else:
                fault_char = char
                break
    return stack, fault_char

score = 0
for line in DATA:
    remaining, fault = isCorrect(line)
    if fault != '':
        score += charsToPoints1[fault]

print(f"Result Part 1: {score}")

#============================= Part Two =============================

scores = []
for line in DATA:
    remaining, fault = isCorrect(line)
    if fault == '':
        score = 0
        for i in range(len(remaining)):
            score *= 5
            score += charsToPoints2[remaining[len(remaining) - 1- i]]
        scores.append(score)

print(f"Result Part 2: {sorted(scores)[int(len(scores)/2)]}")