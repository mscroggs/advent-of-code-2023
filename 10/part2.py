start = None

map = {}
with open("input") as f:
    for y, line in enumerate(f):
        for x, tile in enumerate(line.strip()):
            if tile == "S":
                start = (x, y)
            if tile != ".":
                map[(x, y)] = tile

size = (max(i[0] for i in map) + 1, max(i[1] for i in map) + 1)


def ok(c, d):
    if c not in map:
        return False
    if d == (1,0) and map[c] not in "S-J7":
        return False
    if d == (-1,0) and map[c] not in "S-LF":
        return False
    if d == (0,1) and map[c] not in "S|JL":
        return False
    if d == (0,-1) and map[c] not in "S|F7":
        return False
    return True


connections = {}
pipes = []
for y in range(size[1]):
    for x in range(size[0]):
        if (x, y) in map:
            tile = map[(x, y)]
            if tile == "|":
                n = [(0, 1), (0, -1)]
            elif tile == "-":
                n = [(1, 0), (-1, 0)]
            elif tile == "F":
                n = [(1, 0), (0, 1)]
            elif tile == "7":
                n = [(-1, 0), (0, 1)]
            elif tile == "L":
                n = [(1, 0), (0, -1)]
            elif tile == "J":
                n = [(-1, 0), (0, -1)]

            if (x, y) not in connections:
                connections[(x, y)] = []
            for d in n:
                c = (x+d[0], y+d[1])

                if ok(c, d):
                    if c not in connections:
                        connections[c] = []
                    if (x, y) not in connections[c]:
                        connections[c].append((x, y))
                    if c not in connections[(x, y)]:
                        connections[(x, y)].append(c)

current = [start]
distance = 0
distances = {start: 0}
while True:
    distance += 1
    nc = []
    for c in current:
        for i in connections[c]:
            if i not in distances:
                nc.append(i)
                distances[i] = distance
    current = nc
    if len(nc) == 0:
        break


contained = 0
cls = []
for x in range(size[0]):
    for y in range(size[1]):
        if (x,y) not in distances:
            crosses = [map[(i, y)] for i in range(x) if (i, y) in distances and map[(i, y)] in "LF|J7"]
            while "L" in crosses and "J" in crosses:
                crosses.remove("L")
                crosses.remove("J")
            while "L" in crosses and "7" in crosses:
                crosses.remove("L")
                crosses.remove("7")
                crosses.append("|")
            while "F" in crosses and "7" in crosses:
                crosses.remove("F")
                crosses.remove("7")
            while "F" in crosses and "J" in crosses:
                crosses.remove("F")
                crosses.remove("J")
                crosses.append("|")
            if len(crosses) % 2 == 1:
                cls.append((x, y))
                contained += 1
print(contained)
