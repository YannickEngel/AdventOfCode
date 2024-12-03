DATA = open(f"inputs/input_02.txt").read().split("\n")

num_safe = 0

def check_alt_safe(report, idx):
    #print(report)
    alt_report = report[:idx] + report[idx+1:]
    #print(alt_report)
    incr_ = True if (alt_report[0] - alt_report[1] < 0) else False
    for j in range(len(alt_report) - 1):
        diff_ = alt_report[j] - alt_report[j + 1]
        if not ((diff_ < 0) == incr_ and abs(diff_) >= 1 and abs(diff_) <= 3):
            return False
    return True


for report in DATA:
    #print(report)
    lvls = list(map(lambda x: int(x), report.split(" ")))
    incr = True if (lvls[0] - lvls[1] < 0) else False
    safe = True
    removed = False
    for i in range(len(lvls) - 1):
        diff = lvls[i] - lvls[i + 1]
        #print(diff)
        if not ((diff < 0) == incr and abs(diff) >= 1 and abs(diff) <= 3):
            # on step not safe
            check_alt_start = check_alt_safe(lvls, 0)
            check_alt_lower = check_alt_safe(lvls, i)
            check_alt_upper = check_alt_safe(lvls, i+1)
            if check_alt_lower == check_alt_upper and check_alt_upper == False:
                print(lvls, " ", i)
            safe = check_alt_lower or check_alt_upper or check_alt_start
            break
    if safe:
        #print("safe")
        num_safe += 1

print(num_safe)