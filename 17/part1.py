with open("input") as f:
    map = [[int(i) for i in line.strip()] for line in f]

height = len(map)
width = len(map[0])

shortest = {((0,0), ""): 0}
todo = list(shortest.keys())

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
    new = []
    if d != ">>>" and not d.endswith("<") and x + 1 < width:
        new.append(((x+1, y), d + ">" if d.endswith(">") else ">"))
    if d != "<<<" and not d.endswith(">") and x > 0:
        new.append(((x-1, y), d + "<" if d.endswith("<") else "<"))
    if d != "vvv" and not d.endswith("^") and y + 1 < height:
        new.append(((x, y+1), d + "v" if d.endswith("v") else "v"))
    if d != "^^^" and not d.endswith("v") and y > 0:
        new.append(((x, y-1), d + "^" if d.endswith("^") else "^"))

    for n in new:
        x, y = n[0]
        dist = distance + map[y][x]
        if n not in shortest or dist < shortest[n]:
            if n not in todo:
                todo.append(n)
            shortest[n] = dist
