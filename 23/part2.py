import sys

map = []
start = None
end = (None, -1)

with open("input") as f:
    for y, line in enumerate(f):
        for x, item in enumerate(line.strip()):
            if item != "#":
                if start is None:
                    start = (x, y)
                if y > end[1]:
                    end = (x, y)
                map.append((x, y))

neighbours = {p: [(p[0]+d[0], p[1]+d[1]) for d in [(1,0), (-1,0), (0,1), (0,-1)]
              if (p[0]+d[0], p[1]+d[1]) in map]
              for p in map}

longest = -1

def get_dir_options(p=neighbours[end][0], prev=end, dirs={}, total_distance=0):
    global longest
    distance = 0
    while len(neighbours[p]) == 2:
        distance += 1
        prev, p = p, neighbours[p][0] if prev == neighbours[p][1] else neighbours[p][1]
    if p in dirs:
        return None
    if p == start:
        longest = max(longest, total_distance + distance + len(dirs) + 1)
        print(longest, "".join(dirs.values()))
        return [dirs]

    d = {i:j for i, j in dirs.items()}
    if prev[0] == p[0] + 1:
        d[p] = ">"
    if prev[0] == p[0] - 1:
        d[p] = "<"
    if prev[1] == p[1] + 1:
        d[p] = "v"
    if prev[1] == p[1] - 1:
        d[p] = "^"

    results = []
    for q in neighbours[p]:
        if q != prev:
            o = get_dir_options(q, p, d, total_distance + distance)
            if o is not None:
                results += o
    return results

dirs = get_dir_options()
print(longest)
