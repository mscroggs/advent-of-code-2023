from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


nodes = {}
locations = []
with open("input") as f:
    directions, node_data = f.read().strip().split("\n\n")
    for n in node_data.split("\n"):
        a = n.split(" ")[0]
        b = n.split("(")[1].split(", ")[0]
        c = n.split(", ")[1].split(")")[0]
        nodes[a] = {"L": b, "R": c}
        if a[-1] == "A":
            locations.append(a)

period = len(directions)

options = []

for i in locations:
    n = 0
    visited = []
    z = []
    while True:
        visited.append(i)
        i = nodes[i][directions[n % period]]
        n += 1
        if i[-1] == "Z":
            z.append(n)
        if i in visited[n % period::period]:
            for a, b in enumerate(visited):
                if b == i:
                    assert (len(visited) - a) % period == 0
                    assert len(z) == 1
                    options.append((len(visited) - a, z[0]))
                    break
            else:
                continue
            break

for o in options:
    assert o[0] == o[1]

result = 1
for o in options:
    result = lcm(result, o[0])
print(result)
