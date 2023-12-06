def parse(raw):
    return [tuple(int(a) for a in line.split(" ")) for line in raw.split("\n")]


def get(data, value):
    for i, j, k in data:
        if j <= value < j + k:
            return i + value - j
    return value


def split_range(r, m):
    out = []
    changed = False
    for a, b in r:
        for i, j, k in m:
            if a < j <= b:
                out.append([a, j - 1])
                out.append([j, b])
                changed = True
                break
            elif a <= j + k - 1 < b:
                out.append([a, j+k - 1])
                out.append([j+k, b])
                changed = True
                break
        else:
            out.append([a, b])
    if changed:
        return split_range(out, m)
    else:
        return out


def map_range(r, m):
    return [[get(m, i), get(m, j)] for (i, j) in split_range(r, m)]


with open("input") as f:
    data = f.read()
    seeds = [int(i) for i in data.split("seeds: ")[1].split("\n")[0].split(" ") if i != ""]

    maps = []
    for raw in data.split("\n\n")[1:]:
        maps.append(parse(raw.strip().split("\n", 1)[1]))

r = [(i, i + j - 1) for i, j in zip(seeds[::2], seeds[1::2])]

for m in maps:
    r = map_range(r, m)
print(min(i[0] for i in r))
