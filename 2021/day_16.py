from input_reader import read

input_lines = open(f"inputs/input_16.txt").read()

hexToBinString = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

hexList = list(hexToBinString.keys())
binList = list(hexToBinString.values())

def hexToBinFunc(hex):
    return hexToBinString[hex]

def parseInput(input):
    return ''.join(list(map(hexToBinFunc, input)))

DATA = parseInput(input_lines)

def parseLiteral(input):
    #print(input)
    hexVal = ""
    length = 6
    packetVer = int(input[:3],2)
    packetType = int(input[3:6], 2)
    print(int(input[:3],2))
    input = input[6:]
    lastGroup = False
    while(not lastGroup):
        group = input[:5]
        #print(group)
        if group[0] == "0":
            lastGroup = True
        hexVal += hexList[binList.index(group[1:5])]
        input = input[5:]
        length += 5
    return packetVer, length, int(hexVal, 16)

def exOperator(values, type):
    if type == 0:
        return sum(values)
    if type == 1:
        result = 1
        for i in values:
            result *= i
        return result
    if type == 2:
        return min(values)
    if type == 3:
        return max(values)
    if type == 5:
        if values[0] > values[1]:
            return 1
        else:
            return 0
    if type == 6:
        if values[0] < values[1]:
            return 1
        else:
            return 0
    if type == 7:
        if values[0] == values[1]:
            return 1
        else:
            return 0

def parsePacket(input):
    packetlen = length = index = versionSum = 0
    versionSum += int(input[:3],2)
    print(int(input[:3],2))
    packetType = int(input[3:6], 2)
    input = input[6:]
    packetlen += 6
    values = []
    isLenght = True if input[0] == "0" else False
    if isLenght:
        length = int(input[1:16], 2)
        input = input[16:]
        packetlen +=16
    else:
        length = int(input[1:12],2)
        input = input[12:]
        packetlen += 12
    
   
    while(index < length):
        len = 0
        if(int(input[3:6], 2) == 4):
            #literal
            ...
            vers, len, value = parseLiteral(input)
            versionSum += vers
            values.append(value)
        else:
            #operater
            ...
            vers, len, value = parsePacket(input)
            versionSum += vers
            values.append(value)
        if isLenght:
            index += len
        else:
            index += 1
        input = input[len:]
        packetlen += len
    result = exOperator(values, packetType)
    return versionSum, packetlen, result

def parse(input):
    packetVer = int(input[:3],2)
    packetType = int(input[3:6], 2)
    if packetType != 4:
        return parsePacket(input)
    else:
        return parseLiteral(input)

result = parse(DATA)
print(f"Result Part 1: {result[0]}")
print(f"Result Part 2: {result[2]}")