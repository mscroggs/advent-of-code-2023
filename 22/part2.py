bricks = []
with open("input") as f:
    for line in f:
        a, b = line.strip().split("~")
        bricks.append([tuple(int(i) for i in a.split(",")), tuple(int(i) + 1 for i in b.split(","))])
        assert bricks[-1][0][0] < bricks[-1][1][0]
        assert bricks[-1][0][1] < bricks[-1][1][1]
        assert 0 <= bricks[-1][0][2] < bricks[-1][1][2]

def collide(a, b):
    assert a[0] < a[1]
    assert b[0] < b[1]
    return max(b[0], a[0]) < min(b[1], a[1])

fallen_bricks = []

while len(bricks) > 0:
    min_i = 0
    height = bricks[0][0][2]
    for i, b in enumerate(bricks):
        if b[0][2] < height:
            height = b[0][2]
            min_i = i
    b = bricks[min_i]

    z = 0
    z_i = None
    for i, b2 in enumerate(fallen_bricks):
        if collide((b2[0][0], b2[1][0]), (b[0][0], b[1][0])) and collide((b2[0][1], b2[1][1]), (b[0][1], b[1][1])):
            z = max(z, b2[1][2])
            z_i = i

    fallen_bricks.append([(b[0][0], b[0][1], z), (b[1][0], b[1][1], z + b[1][2] - b[0][2]), True])
    bricks = bricks[:min_i] + bricks[min_i + 1:]

    assert fallen_bricks[-1][0][0] < fallen_bricks[-1][1][0]
    assert fallen_bricks[-1][0][1] < fallen_bricks[-1][1][1]
    assert fallen_bricks[-1][0][2] < fallen_bricks[-1][1][2]


supports = [[] for b in fallen_bricks]
for i, b in enumerate(fallen_bricks):
    for j, b2 in enumerate(fallen_bricks):
        if i == j:
            continue
        if b2[1][2] == b[0][2] and collide((b2[0][0], b2[1][0]), (b[0][0], b[1][0])) and collide((b2[0][1], b2[1][1]), (b[0][1], b[1][1])):
            supports[i].append(j)

out = 0
for i, _ in enumerate(fallen_bricks):
    fallen = [i]
    nf = [i]
    while len(nf) > 0:
        nf = []
        for j, s in enumerate(supports):
            if j not in fallen and len(s) > 0:
                for k in s:
                    if k not in fallen:
                        break
                else:
                    nf.append(j)
        fallen += nf
    out += len(fallen) - 1

print(out)
