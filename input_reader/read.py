def inputLines(day):
    lines = open(f"input_reader/inputs/input_{day:02}.txt").readlines()
    newlines= []
    for i in range (len(lines)):
        if i != len(lines) - 1:
            newlines.append(lines[i][:-1])
        else:
            newlines.append(lines[i])
    return newlines

def input(day):
    return open(f"input_reader/inputs/input_{day:02}.txt").read()

def testInputLines(day):
    lines = open(f"input_reader/inputs/test_input_{day:02}.txt").readlines()
    newlines= []
    for i in range (len(lines)):
        if i != len(lines) - 1:
            newlines.append(lines[i][:-1])
        else:
            newlines.append(lines[i])
    return newlines

def testInput(day):return open(f"input_reader/inputs/test_input_{day:02}.txt").read()