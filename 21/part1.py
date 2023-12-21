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

reachable = [start]
for _ in range(64):
    print(_, len(reachable))
    new_r = []
    for p in reachable:
        for d in [(1,0), (0,1), (-1,0), (0,-1)]:
            p2 = (p[0] + d[0], p[1] + d[1])
            if p2 in spaces and p2 not in new_r:
                new_r.append(p2)
    reachable = new_r

print(len(reachable))
