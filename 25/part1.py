from itertools import product

connections = []
nodes = set()

with open("input") as f:
    for line in f:
        a, b = line.strip().split(": ")
        nodes.add(a)
        for c in b.split():
            nodes.add(c)
            connections.append([a, c])

nodes = list(nodes)
neighbours = {n: [c[0] for c in connections if c[1] == n] + [c[1] for c in connections if c[0] == n]
              for n in nodes}


def nunique_paths(a, b):
    used = []
    n = 0
    while True:
        distances = {i: [] for i in a}
        done = []
        while len(done) < len(distances):
            if b in distances:
                n += 1
                if n > 3:
                    return n
                used += distances[b]
                break
            next_d = 100000
            next = None
            for i, j in distances.items():
                if i not in done:
                    if len(j) < next_d:
                        next_d = len(j)
                        next = i
            if next_d > 3 + 3**n:
                return n
            next_path = distances[next]
            done.append(next)
            for m in neighbours[next]:
                if m not in done and {next, m} not in used:
                    if m not in distances or len(next_path) + 1 < len(distances[m]):
                        distances[m] = next_path + [{next, m}]
        else:
            break
    return n

groups = []

remaining_nodes = [n for n in nodes]

while len(remaining_nodes) > 0:
    g = [remaining_nodes[0]]
    addme = []
    for i, a in enumerate(remaining_nodes[1:]):
        print(i, len(remaining_nodes), len(addme))
        if nunique_paths(g, a) > 3:
            addme.append(a)
    g += addme
    for a in g:
        remaining_nodes.remove(a)
    groups.append(g)

for halves in product([False, True], repeat=len(groups)):
    if True not in halves or False not in halves:
        continue

    h = {n: h for g, h in zip(groups, halves) for n in g}
    if len([c for c in connections if h[c[0]] != h[c[1]]]) <= 3:
        break

print(len([n for g, h in zip(groups, halves) for n in g if h]) * len([n for g, h in zip(groups, halves) for n in g if not h]))
