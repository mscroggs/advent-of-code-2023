map = []

with open("input") as f:
    for line in f:
        map.append([i for i in line.strip()])

width = len(map[0])
height = len(map)

max_v = 0

for start in [
    ((-1,y), "x+") for y in range(height)
] + [
    ((width,y), "x-") for y in range(height)
] + [
    ((x, -1), "y+") for x in range(width)
] + [
    ((x, height), "y-") for x in range(width)
]:
    visited = []
    done = []
    current = [start]

    while len(current) > 0:
        nc = []
        for p, d in current:
            if (p, d) in done:
                continue
            done.append((p, d))
            if d == "x+":
                p = (p[0] + 1, p[1])
            elif d == "x-":
                p = (p[0] - 1, p[1])
            elif d == "y+":
                p = (p[0], p[1] + 1)
            else:
                assert d == "y-"
                p = (p[0], p[1] - 1)
            if 0 <= p[0] < width and 0 <= p[1] < height:
                tile = map[p[1]][p[0]]
                if tile == "/":
                    d = {"x+": "y-", "x-": "y+", "y-": "x+", "y+": "x-"}[d]
                    nc.append((p, d))
                elif tile == "\\":
                    d = {"x+": "y+", "x-": "y-", "y-": "x-", "y+": "x+"}[d]
                    nc.append((p, d))
                elif tile == "|":
                    if d.startswith("y"):
                        nc.append((p, d))
                    else:
                        nc.append((p, "y+"))
                        nc.append((p, "y-"))
                elif tile == "-":
                    if d.startswith("x"):
                        nc.append((p, d))
                    else:
                        nc.append((p, "x+"))
                        nc.append((p, "x-"))
                else:
                    assert tile == "."
                    nc.append((p, d))

        for p, d in nc:
            if p not in visited:
                visited.append(p)

        current = nc

    print(start, len(visited))
    max_v = max(max_v, len(visited))
print(max_v)
