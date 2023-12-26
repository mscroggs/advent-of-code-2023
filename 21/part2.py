spaces = []
start = None
with open("input") as f:
    for y, line in enumerate(f):
        for x, entry in enumerate(line.strip()):
            if entry == "S":
                start = (x, y)
                spaces.append((x, y))
            elif entry == ".":
                spaces.append((x, y))

width = 1 + max(x for x, y in spaces)
height = 1 + max(y for x, y in spaces)
print(width,height)

assert width == height
n = (width - 1) // 2

reachable = {start}
prev = set()
np = {start}

indices = []
sizes = []
diffs = []
diff2s = []
diff3s = []

i = 0
while True:
    print(i, len(reachable))
    i += 1
    new_r = set()
    for r in prev:
        new_r.add(r)
    newest = set()
    for p in np:
        for d in [(1,0), (0,1), (-1,0), (0,-1)]:
            p2 = (p[0] + d[0], p[1] + d[1])
            p2w = (p2[0] % width, p2[1] % height)
            if p2w in spaces:
                new_r.add(p2)
                if p2 not in prev:
                    newest.add(p2)
    np = newest
    prev, reachable = reachable, new_r

    if i % width == n:
        indices.append(i)
        sizes.append(len(new_r))
        if len(sizes) >= 2:
            diffs.append(sizes[-1] - sizes[-2])
        if len(diffs) >= 2:
            diff2s.append(diffs[-1] - diffs[-2])

        if len(diff2s) > 0:
            break

assert diff2s[-1] % 2 == 0
a = diff2s[-1] // 2
b = (sizes[-1] - a * ((indices[-1] - n) // width) ** 2) - (sizes[-2] - a * ((indices[-2] - n) // width) ** 2)
c = 0
c = sizes[-1] - (a * ((indices[-1] - n) // width) ** 2 + b * ((indices[-1] - n) // width))


steps = 26501365

assert (steps - n) % width == 0
i = (steps - n) // width

print(a * i ** 2 + b * i + c)
