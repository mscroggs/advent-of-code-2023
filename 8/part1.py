nodes = {}
with open("input") as f:
    directions, node_data = f.read().strip().split("\n\n")
    for n in node_data.split("\n"):
        a = n.split(" ")[0]
        b = n.split("(")[1].split(", ")[0]
        c = n.split(", ")[1].split(")")[0]
        nodes[a] = {"L": b, "R": c}

location = "AAA"
n = 0
while location != "ZZZ":
    location = nodes[location][directions[n % len(directions)]]
    n += 1
print(n)
