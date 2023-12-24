lines = []

min_x = 200000000000000
min_y = 200000000000000
max_x = 400000000000000
max_y = 400000000000000

with open("input") as f:
    for line in f:
        p, v = line.strip().split(" @ ")
        p = [int(i) for i in p.split(", ")]
        v = [int(i) for i in v.split(", ")]
        lines.append([p, v])

count = 0
N = 0
for i, (p0, v0) in enumerate(lines):
    for p1, v1 in lines[i+1:]:
        if v0[1] - v0[0] * v1[1] /  v1[0] == 0:
            continue
        b = (p1[1] + (p0[0] - p1[0]) * v1[1] / v1[0] - p0[1]) / (v0[1] - v0[0] * v1[1] /  v1[0])
        a = (p0[0] + b * v0[0] - p1[0]) / v1[0]

        if a >= 0 and b >= 0:
            intersection = [
                p1[i] + a * v1[i]
                for i in range(2)
            ]
            if min_x <= intersection[0] <= max_x and min_y <= intersection[1] <= max_y:
                count += 1
print(count)
