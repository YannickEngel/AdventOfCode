input = open(f"inputs/input_06.txt").read()

# =========================== Part 1 ================================

for i in range(len(input) - 4):
    if(len([*set(input[i: i+4])]) == 4):
        print("Part 1: ", i+4)
        break

# =========================== Part 2 ================================

for i in range(len(input) - 14):
    if(len([*set(input[i: i+14])]) == 4):
        print("Part 2: ", i+14)
        break