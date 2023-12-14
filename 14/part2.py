rocks = []
barriers = []
height = 0
width = 0
with open("input") as f:
    for y, line in enumerate(f):
        height += 1
        width = len(line.strip())
        for x, item in enumerate(line.strip()):
            if item == "O":
                rocks.append([x, y])
            if item == "#":
                barriers.append([x, y])

positions = []
N = 1000000000
for c in range(N):
    # N
    for i, (x, y) in enumerate(rocks):
        rocks[i][1] = max([0] + [j[1] + 1 for j in rocks[:i] + barriers if j[0] == x and j[1] < y] )

    # W
    rocks.sort(key=lambda i: i[0])
    for i, (x, y) in enumerate(rocks):
        rocks[i][0] = max([0] + [j[0] + 1 for j in rocks[:i] + barriers if j[1] == y and j[0] < x])

    # S
    rocks.sort(key=lambda i: -i[1])
    for i, (x, y) in enumerate(rocks):
        rocks[i][1] = min([height - 1] + [j[1] - 1 for j in rocks[:i] + barriers if j[0] == x and j[1] > y])

    # E
    rocks.sort(key=lambda i: -i[0])
    for i, (x, y) in enumerate(rocks):
        rocks[i][0] = min([width - 1] + [j[0] - 1 for j in rocks[:i] + barriers if j[1] == y and j[0] > x])

    rocks.sort(key=lambda i: i[1])

    if rocks in positions:
        i = positions.index(rocks)
        rocks = positions[i + (N - 1 - i) % (c - i)]
        break
    positions.append([[j for j in i] for i in rocks])

load = 0
for (x, y) in rocks:
    load += height - y
print(load)
