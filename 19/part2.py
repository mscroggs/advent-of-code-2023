from itertools import product
import json

workflows = {}

with open("input") as f:
    w, _ = f.read().split("\n\n")
    for i in w.split("\n"):
        name, c = i.split("{")
        conditions = []
        for j in c[:-1].split(","):
            if ":" in j:
                a, b = j.split(":")
                assert "=" not in a
                if "<" in a:
                    c, d = a.split("<")
                    conditions.append((c, "<", int(d), b))
                else:
                    c, d = a.split(">")
                    conditions.append((c, ">", int(d), b))
            else:
                conditions.append((None, None, None, j))
        workflows[name] = conditions


options = [({i: [1, 4001] for i in "xmas"}, "in")]

while len([i for i in options if i[1] not in "RA"]) > 0:
    new_options = []
    for v, id in options:
        if id in "RA":
            new_options.append((v, id))
        else:
            for i, j, k, l in workflows[id]:
                if i is None:
                    new_options.append((v, l))
                else:
                    if j == "<":
                        v1 = {a: [b[0], k] if a == i else b for a, b in v.items()}
                        v = {a: [k, b[1]] if a == i else b for a, b in v.items()}
                        new_options.append((v1, l))
                    else:
                        v1 = {a: [k + 1, b[1]] if a == i else b for a, b in v.items()}
                        v = {a: [b[0], k + 1] if a == i else b for a, b in v.items()}
                        new_options.append((v1, l))
    options = new_options

total = 0
for a, b in options:
    if b == "A":
        n = 1
        for i, j in a.values():
            n *= j - i
        total += n
print(total)
