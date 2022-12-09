import re

input = open(f"inputs/input_21.txt").read()

def parseInput(input):
    return [(int(pos) - 1) for pos in re.findall(r": (\d)", input)]

BOARDPOS = parseInput(input)

#============================= Part One =============================
playerPoints = [0,0]
player = 0
dice = 1
diceRolls = 0
playerPos = BOARDPOS.copy()

while(playerPoints[0] < 1000 and playerPoints[1] < 1000):
    
    rolled = 0
    for i in range(3):
        if dice <= 100:
            rolled += dice
        else:
            dice = (dice % 100)
            rolled += dice
        diceRolls += 1
        dice += 1
    playerPos[player] = (playerPos[player] + rolled) % 10
    playerPoints[player] += playerPos[player] + 1

    player = 0 if player == 1 else 1
losingPlayer = 0 if playerPoints[1] >= 1000 else 1

print("Part 1: ", diceRolls * playerPoints[losingPlayer])
#============================= Part Two =============================
