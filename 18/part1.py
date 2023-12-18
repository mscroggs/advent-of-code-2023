dug = []
pos = [0,0]
with open("input") as f:
    for line in f:
        d, n, _ = line.split()
        for i in range(int(n)):
            if d == "U":
                pos[1] -= 1
            elif d == "D":
                pos[1] += 1
            elif d == "L":
                pos[0] -= 1
            else:
                assert d == "R"
                pos[0] += 1
            dug.append(tuple(pos))

assert dug[-1] == (0,0)

xrange = (min(i[0] for i in dug), max(i[0] for i in dug) + 1)
yrange = (min(i[1] for i in dug), max(i[1] for i in dug) + 1)

interior = 0

for y in range(*yrange):
    dr = [i[0] for i in dug if i[1] == y]
    dr0 = [i[0] for i in dug if i[1] == y - 1]
    dr2 = [i[0] for i in dug if i[1] == y + 1]
    for x in range(*xrange):
        if x not in dr:
            n = 0
            xx = xrange[0] - 1
            while xx <= x:
                if xx in dr:
                    below = xx in dr2
                    above = xx in dr0
                    xx += 1
                    while xx in dr:
                        xx += 1
                    if ((xx - 1 in dr2) and above) or ((xx - 1 in dr0) and below):
                        n += 1
                else:
                    xx += 1
            if n % 2 == 1:
                interior += 1

print(len(dug) + interior)
