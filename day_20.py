from input_reader import read
import numpy as np

input_lines = read.input(20)


def parseInput(input):
    imgEnh, image = input.split('\n\n')
    img = []
    for line in image.split('\n'):
        imgGrid = [char for char in line]
        img.append(imgGrid)
    return imgEnh, img

IMGENH, IMG = parseInput(input_lines)
INFPIX = '.'
#============================= Part One =============================

def paddGrid(grid):
    newGrid = []
    for i in range(len(grid) + 2):
        newLine = []
        for j in range(len(grid[0]) + 2):
            if i == 0 or i == len(grid) + 1 or j == 0 or j == len(grid[0]) + 1:
                newLine.append(INFPIX)
            else:
                newLine.append(grid[i-1][j-1])
        newGrid.append(newLine)
    return newGrid

def imgEnhPos(grid, x, y):
    bitString = ""
    for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1):
        if 0 <= x+dx <len(grid) and 0<=y+dy<len(grid[x]):
            bit = "0" if grid[x+dx][y+dy] == '.' else "1"
        else:
            bit = "0" if INFPIX == '.' else "1"
        bitString += bit
    return int(bitString, 2)

def doStep(oldGrid):
    grid = paddGrid(oldGrid)
    newGrid = []
    for i in range(len(grid[0])):
        newLine = []
        for j in range(len(grid[i])):
            enhPos = imgEnhPos(grid, i, j)
            newLine.append(IMGENH[enhPos])
        newGrid.append(newLine)
    return newGrid


Initial_Grid = paddGrid(IMG)


img = doStep(Initial_Grid)
INFPIX = IMGENH[0] if INFPIX == '.' else IMGENH[255]
img = doStep(img)
INFPIX = IMGENH[0] if INFPIX == '.' else IMGENH[255]
count = np.count_nonzero(np.array(img) =='#')
print(f"Result Part 1: {count}")


#============================= Part Two =============================

for i in range(50):
    if i == 0:
        img = doStep(Initial_Grid)
    else:
        img = doStep(img)
    INFPIX = IMGENH[0] if INFPIX == '.' else IMGENH[255]
count = np.count_nonzero(np.array(img) =="#")
print(f"Result Part 2: {count}")