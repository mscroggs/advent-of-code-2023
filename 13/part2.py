with open("input") as f:
    patterns = [[[j for j in i] for i in p.split("\n") if i != ""]
                for p in f.read().split("\n\n")]

result = 0
for p in patterns:
    noth = None
    notv = None
    for i in range(1, len(p)):
        l = min(i, len(p) - i)
        if p[i - l:i] == p[i:i + l][::-1]:
            noth = i
            break
    else:
        for i in range(1, len(p[0])):
            l = min(i, len(p[0]) - i)
            if [j[i - l:i] for j in p] == [j[i:i + l][::-1] for j in p]:
                notv = i
                break
        else:
            raise ValueError()
    hashes = [(i, j) for i, row in enumerate(p) for j, entry in enumerate(row) if entry == "#"]

    for h in hashes:
        p[h[0]][h[1]] = "."
        for i in range(1, len(p)):
            if i != noth:
                l = min(i, len(p) - i)
                if p[i - l:i] == p[i:i + l][::-1]:
                    result += 100 * i
                    break
        else:
            for i in range(1, len(p[0])):
                if i != notv:
                    l = min(i, len(p[0]) - i)
                    if [j[i - l:i] for j in p] == [j[i:i + l][::-1] for j in p]:
                        result += i
                        break
            else:
                p[h[0]][h[1]] = "#"
                continue
        break
print(result)
