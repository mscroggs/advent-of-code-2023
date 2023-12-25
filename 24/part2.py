def dot(v, w):
    return sum(i * j for i, j in zip(v, w))

def cross(v, w):
    return [
        v[1] * w[2] - v[2] * w[1],
        v[2] * w[0] - v[0] * w[2],
        v[0] * w[1] - v[1] * w[0],
    ]

lines = []

with open("input") as f:
    for line in f:
        p, v = line.strip().split(" @ ")
        p = [int(i) for i in p.split(", ")]
        v = [int(i) for i in v.split(", ")]
        lines.append([p, v])

p = [i for i in p]
v = [i for i in v]

for i, _ in enumerate(lines):
    lines[i][0] = [i - j for i, j in zip(lines[i][0], p)]
    lines[i][1] = [i - j for i, j in zip(lines[i][1], v)]

normal = cross(lines[1][0], lines[1][1])

i2 = -dot(lines[2][0], normal) // dot(lines[2][1], normal)
pt2 = [i + i2 * j for i, j in zip(*lines[2])]
i3 = -dot(lines[3][0], normal) // dot(lines[3][1], normal)
pt3 = [i + i3 * j for i, j in zip(*lines[3])]

pt2_actual = [i + j + i2 * k for i, j, k in zip(pt2, p, v)]
pt3_actual = [i + j + i3 * k for i, j, k in zip(pt3, p, v)]

d = [(i - j) // (i2 - i3) for i, j in zip(pt2_actual, pt3_actual)]
start = [i - i2 * j for i, j in zip(pt2_actual, d)]
print(sum(start))
