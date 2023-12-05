def parse(raw):
    return [tuple(int(a) for a in line.split(" ")) for line in raw.split("\n")]


def get(data, value):
    for i, j, k in data:
        if j <= value < j + k:
            return i + value - j
    return value


with open("input") as f:
    data = f.read()
    seeds = [int(i) for i in data.split("seeds: ")[1].split("\n")[0].split(" ") if i != ""]

    maps = []
    for raw in data.split("\n\n")[1:]:
        maps.append(parse(raw.strip().split("\n", 1)[1]))

smallest = None
for s in seeds:
    for m in maps:
        s = get(m, s)
    if smallest is None or s < smallest:
        smallest = s
print(smallest)
