galaxies = []
with open("input") as f:
    for y, line in enumerate(f):
        for x, item in enumerate(line.strip()):
            if item == "#":
                galaxies.append((x, y))

x = 0
while x <= max(i[0] for i in galaxies):
    if len([i for i in galaxies if i[0] == x]) == 0:
        galaxies = [(i[0] + 999999, i[1]) if i[0] > x else i for i in galaxies]
        x += 999999
    x += 1

y = 0
while y <= max(i[1] for i in galaxies):
    if len([i for i in galaxies if i[1] == y]) == 0:
        galaxies = [(i[0], i[1] + 999999) if i[1] > y else i for i in galaxies]
        y += 999999
    y += 1

total = 0
for i, g in enumerate(galaxies):
    for h in galaxies[:i]:
        total += abs(g[0] - h[0]) + abs(g[1] - h[1])
print(total)
