import json

workflows = {}
parts = []

with open("input") as f:
    w, p = f.read().split("\n\n")
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

    for i in p.split("\n"):
        if i != "":
            parts.append({a.split("=")[0]: int(a.split("=")[1]) for a in i[1:-1].split(",")})


def process(p, id="in"):
    if id == "R":
        return False
    if id == "A":
        return True

    for i, j, k, l in workflows[id]:
        if i is None or (j == "<" and p[i] < k) or (j == ">" and p[i] > k):
            return process(p, l)

    raise RuntimeError()


total = 0
for p in parts:
    if process(p):
        total += sum(p.values())
print(total)
