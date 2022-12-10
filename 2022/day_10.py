input = open(f"inputs/input_10.txt").read().split("\n")

val = 0
cycle = 0
x = 0
stre = []
check = [20 + i * 40 for i in range(6) ]
spriteStart = 0
screen = [["." for i in range(40)] for j in range(6)]

print(check)
for line in input:
    if(line == "noop"):
        screen[int(cycle / 40)][cycle % 40] = '#' if (cycle % 40) >= x and (cycle % 40) <= x + 2 else '.'
        cycle += 1
        cycle = cycle % 240
        if(cycle in check):
            stre.append(cycle*x)
    else:
        for i in range(2):
            screen[int(cycle / 40)][cycle % 40] = '#' if (cycle % 40) >= x and (cycle % 40) <= x + 2 else '.'
            cycle += 1
            cycle = cycle % 240
            if(cycle in check):  
                stre.append(cycle*x)
        x += int(line.split(" ")[1])




print("Part 1: ", sum(stre))

print("Part 2:")
for line in ["".join([ch if ch == "#" else " " for ch in line]) for line in screen]:
    print("   ".join([line[:4], line[5:9], line[10:14], line[15:19], line[20:24], line[25:29], line[30:34], line[35:39]]))


