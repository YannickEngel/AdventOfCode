import re

DATA = [((int(fstLow), int(fstHigh)), (int(sndLow),int(sndHigh))) for fstLow, fstHigh, sndLow, sndHigh in re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", open(f"inputs/input_04.txt").read())]

# =========================== Part 1 ================================

fully_contained = 0
for pair in DATA:
    small, big = (pair[0], pair[1]) if pair[0][1] - pair[0][0] <= pair[1][1] - pair[1][0] else (pair[1], pair[0])
    if ((small[0] >= big[0] and small[1] <= big[1])):
        fully_contained +=1

print("Part 1: ", fully_contained)

# =========================== Part 2 ================================

overlap = 0
for pair in DATA:
    fst, snd = pair
    if (not (fst[0] > snd[1] or fst[1] < snd[0])):
        overlap +=1

print("Part 2: ", overlap)