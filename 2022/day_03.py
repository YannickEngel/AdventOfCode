

input = open(f"inputs/input_03.txt").readlines()

def calcSum(array):
    sum = 0
    for ch in array:
        if(ord(ch) < 91): #uppercase
            sum += ord(ch) - ord('A') + 27 
        else:
            sum += ord(ch)- (ord('a')) + 1
    return sum

#=========== Part 1 ==============

duplicates = []
for line in input:
    part1 = line[:int(len(line)/2)]
    part2 = line[int(len(line)/2):]
    lineDuplicates = set()
    for i in range(len(part1)):
        if(part1[i] in part2):
            lineDuplicates.add(part1[i])
    duplicates += [item for item in lineDuplicates]

print("Part 1: ", calcSum(duplicates))

#=========== Part 2 ==============

badges = []
for i in range(int(len(input)/3)):
    for ch in input[3*i]:
        if(ch in input[3*i +1] and ch in input[3*i + 2]):
            badges.append(ch)
            break
sum = 0

print("Part 2: ", calcSum(badges))



