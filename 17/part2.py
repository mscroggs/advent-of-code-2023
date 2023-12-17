with open("input") as f:
    map = [[int(i) for i in line.strip()] for line in f]

height = len(map)
width = len(map[0])

shortest = {((0,0), ""): 0}
done = {}
todo = list(shortest.keys())

a = 0

while True:
    next = None
    minimum = None
    for i in todo:
        j = shortest[i]
        if minimum is None or j < minimum:
            next = i
            minimum = j
    (x, y), d = next
    distance = shortest[next]
    if x == width - 1 and y == height - 1:
        print(distance)
        break
    todo.remove(next)
    if (x, y) not in done:
        done[(x, y)] = []
    for dd, dist in done[(x, y)]:
        if d.endswith(dd) and dist < distance:
            break
    else:
        done[(x, y)].append((d, distance))
        new = {}
        if d != ">"*10 and not d.endswith("<"):
            if d.endswith(">"):
                if x + 1 < width:
                    new[((x+1, y), d + ">")] = distance + map[y][x+1]
            elif x + 4 < width:
                new[((x+4, y), ">>>>")] = distance + sum(map[y][x+1:x+5])
        if d != "<"*10 and not d.endswith(">"):
            if d.endswith("<"):
                if x > 0:
                    new[((x-1, y), d + "<")] = distance + map[y][x-1]
            elif x - 4 >= 0:
                new[((x-4, y), "<<<<")] = distance + sum(map[y][x-4:x])
        if d != "v"*10 and not d.endswith("^"):
            if d.endswith("v"):
                if y + 1 < height:
                    new[((x, y+1), d + "v")] = distance + map[y+1][x]
            elif y + 4 < height:
                new[((x, y+4), "vvvv")] = distance + sum(m[x] for m in map[y+1:y+5])
        if d != "^"*10 and not d.endswith("v"):
            if d.endswith("^"):
                if y > 0:
                    new[((x, y-1), d + "^")] = distance + map[y-1][x]
            elif y - 4 >= 0:
                new[((x, y-4), "^^^^")] = distance + sum(m[x] for m in map[y-4:y])

        for n, dist in new.items():
            if n not in shortest or dist < shortest[n]:
                if n not in todo:
                    todo.append(n)
                shortest[n] = dist
