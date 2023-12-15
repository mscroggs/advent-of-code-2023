with open("input") as f:
    strs = f.read().strip().split(",")


def hash(s):
    n = 0
    for c in s:
        n += ord(c)
        n *= 17
        n %= 256
    return n


contents = {}

for s in strs:
    if "-" in s:
        label = s.split("-")[0]
        box = hash(label)
        if box in contents:
            contents[box] = [i for i in contents[box] if i[0] != label]
    elif "=" in s:
        label, n = s.split("=")
        n = int(n)
        box = hash(label)
        if box not in contents:
            contents[box] = []
        for i, j in enumerate(contents[box]):
            if j[0] == label:
                contents[box][i] = (label, n)
                break
        else:
            contents[box].append((label, n))
    else:
        raise ValueError()

total = 0
for n, c in contents.items():
    for i, j in enumerate(c):
        total += (n + 1) * (i + 1) * j[1]
print(total)
