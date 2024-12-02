DATA = list(map(lambda x: list(map(lambda x1: int(x1), x)) ,list(map(lambda x: x[:-1].split("   "), open(f"inputs/input_01.txt").readlines()))))

fst = sorted([numb for [numb, _] in DATA])
snd = sorted([numb for [_, numb] in DATA])

sum_diff = 0
for i in range(len(fst)):
    sum_diff += abs(fst[i] - snd[i])

print("Part1: ", sum_diff)

counts = dict()
for i in snd:
    if i in counts.keys():
        counts[i] += 1
    else:
        counts[i] = 1

sim_score = 0
for i in fst:
    sim_score += i * counts[i] if i in counts.keys() else 0

print("Part2", sim_score)