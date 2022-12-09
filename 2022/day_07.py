
from collections import defaultdict

input = [line[:-1] for line in open(f"inputs/input_07.txt").readlines()]

dirStack = []
currentDir = ''
dirSize = defaultdict(int)

ind = 0

while ind < len(input):

    if(input[ind][:4] == "$ cd"):
        # change dir and update dir path
        dr = input[ind][5:]
        if(dr == ".."):
            dirStack.pop()
            currentDir = dirStack[-1]
        else:
            currentDir = dr
            dirStack.append(dr)
        ind = ind + 1 

    if(input[ind][:4] == "$ ls"):
        # add up sizes of files and add to current dir and all dirs on path
        ind = ind + 1
        while(input[ind][0] != "$"):
            if(input[ind].split(" ")[0] == "dir"):          
                ind = ind + 1
                continue
            sz = int(input[ind].split(" ")[0])
            for i in range(1, len(dirStack)+1):
                dirSize['/'.join(dirStack[:i])] += sz
            ind = ind + 1
            if(ind >= len(input)):
                break

total = dirSize['/']
needFree = total - 40000000

part1 = 0
part2 = 40000000
for _,size in dirSize.items():
    if size <= 100000:
        part1 += size
    if size >= needFree:
        part2 = min(size, part2)

print("Part 1: ", part1)
print("Part 2: ", part2)