nexts = 0

with open("input") as f:
    for line in f:
        numbers = [int(i) for i in line.strip().split()]

        diffs = [numbers]
        while max(diffs[-1]) != min(diffs[-1]) or diffs[-1][0] != 0:
            diffs.append([j-i for i, j in zip(diffs[-1][:-1], diffs[-1][1:])])

        diffs[-1].append(0)
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].append(diffs[i][0] - diffs[i+1][-1])
        nexts += diffs[0][-1]
print(nexts)
