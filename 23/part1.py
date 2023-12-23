import sys

map = {}
start = None
max_y = -1

with open("input") as f:
    for y, line in enumerate(f):
        for x, item in enumerate(line.strip()):
            if item != "#":
                if start is None:
                    start = (x, y)
                map[(x, y)] = item
                max_y = max(max_y, y)

sys.setrecursionlimit(len(map))


def longest_walk(done=[start]):
    x, y = done[-1]
    if y == max_y:
        return len(done)
    tile = map[(x, y)]
    if tile == ">":
        if (x+1, y) in done:
            return -1
        return longest_walk(done + [(x+1, y)])
    if tile == "<":
        if (x-1, y) in done:
            return -1
        return longest_walk(done + [(x-1, y)])
    if tile == "^":
        if (x, y-1) in done:
            return -1
        return longest_walk(done + [(x, y-1)])
    if tile == "v":
        if (x, y+1) in done:
            return -1
        return longest_walk(done + [(x, y+1)])

    longest = -1
    for d in [(1,0), (-1,0), (0,1), (0,-1)]:
        new = (x+d[0], y+d[1])
        if new not in done and new in map:
            longest = max(longest, longest_walk(done + [new]))
    return longest


print(longest_walk() - 1)
