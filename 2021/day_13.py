import numpy as np

input_lines = open(f"inputs/input_13.txt").read()

def parseInput(input):
    temp = []
    temp1 = []
    temp2 = []
    for line in input:
        if line == '':
            ...
        elif line[0] == "f":
            slp = line.split(' ')[2].split('=')
            if slp[0] == 'x':
                temp1.append(int(slp[1]))
            else:
                temp2.append(int(slp[1]))
        else:
            [x,y] = line.split(',')
            temp.append((int(x), int(y)))
    return temp, temp1, temp2

DATA = parseInput(input_lines)

points = DATA[0]
x_flods = DATA[1]
y_flods = DATA[2]

arg_max_x = arg_max_y = 0
for x,y in points:
    if arg_max_x < x:
        arg_max_x = x
    elif arg_max_y < y:
        arg_max_y = y
arg_max_x += 1
arg_max_y += 2

def printMatrix(mat):
    for line in mat:
        print(''.join(list(map(lambda x: '.' if x == 0 else '#', line))))

#============================= Part One =============================

manual = np.zeros((arg_max_y,arg_max_x))
for (x,y) in points:
    manual[y][x] = 1

def fold_horizonzal(mat, pos):
    y, x = mat.shape[0] - 1, mat.shape[1] -1
    newY = pos
    new = []
    for i in range(newY):
        line = mat[i] + mat[y - i]
        new.append(line)
    return (np.where(np.array(new) > 0, 1, 0))

def fold_vertical(mat, pos):
    y, x = mat.shape[0], mat.shape[1] - 1
    newX = pos
    newline = [[0] * newX][0]
    new = []
    for i in range(y):
        new.append(newline)
    newM = np.array(new)
    for i in range(y):
        for j in range(newX):
            newM[i, j] = mat[i,j] + mat[i,x - j]
    return (np.where(np.array(newM) > 0, 1, 0))


man = fold_vertical(manual, x_flods[0])

print(np.count_nonzero(man))

#============================= Part Two =============================

man = manual

for i in range(5):
    man = fold_vertical(man, x_flods[i])
    man = fold_horizonzal(man, y_flods[i])

man = fold_horizonzal(man, y_flods[5])
man = fold_horizonzal(man, y_flods[6])

printMatrix(man)

