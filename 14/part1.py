rocks = []
barriers = []
height = 0
with open("input") as f:
    for y, line in enumerate(f):
        height += 1
        for x, item in enumerate(line.strip()):
            if item == "O":
                rocks.append((x, y))
            if item == "#":
                barriers.append((x, y))

old_rocks = []
while old_rocks != rocks:
    old_rocks = [i for i in rocks]
    rocks = []
    for (x, y) in old_rocks:
        if y == 0 or (x, y-1) in rocks + barriers:
            rocks.append((x, y))
        else:
            rocks.append((x, y-1))

load = 0
for (x, y) in rocks:
    load += height - y
print(load)
