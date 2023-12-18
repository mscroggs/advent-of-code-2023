dug = {}
pos = [0,0]
dcount = 0
xmin = 0
xmax = 0
ymin = 0
ymax = 0
with open("input") as f:
    for line in f:
        _, _, c = line.split()
        c = c.split("(#")[1].split(")")[0]
        d = "RDLU"[int(c[-1])]
        n = int(c[:-1], 16)

        for i in range(n):
            if d == "U":
                pos[1] -= 1
            elif d == "D":
                pos[1] += 1
            elif d == "L":
                pos[0] -= 1
            else:
                assert d == "R"
                pos[0] += 1
            if pos[1] not in dug:
                dug[pos[1]] = []
            dug[pos[1]].append(pos[0])
            dcount += 1
        xmin = min(xmin, pos[0])
        xmax = max(xmax, pos[0])
        ymin = min(ymin, pos[1])
        ymax = max(ymax, pos[1])

assert pos == [0,0]

xrange = (xmin, xmax + 1)
yrange = (ymin, ymax + 1)
dug = [[]] + [sorted(dug[y]) for y in range(*yrange)] + [[]]

pt = [sum(xrange) // 2, sum(yrange) // 2 + 1]

interior = 0

for dr0, dr, dr2 in zip(dug, dug[1:], dug[2:]):
    inside = False
    inside_start = None
    mid = 0
    i = 0
    while i < len(dr):
        x0 = dr[i]
        while i+1 < len(dr) and dr[i+1] == dr[i] + 1:
            i += 1
        x1 = dr[i]
        if (x0 in dr0 and x1 in dr2) or (x1 in dr0 and x0 in dr2):
            if inside:
                interior += x0 - inside_start
                inside = False
            else:
                inside_start = x1 + 1
                inside = True
                mid = 0
        else:
            if inside:
                interior += x0 - inside_start
                inside_start = x1 + 1
        i += 1
print(dcount + interior)
