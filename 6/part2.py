with open("input") as f:
    t, d = f.read().strip().split("\n")
    t = int("".join(t.split()[1:]))
    d = int("".join(d.split()[1:]))

count = 0
for hold in range(t + 1):
    distance = hold * (t - hold)
    if distance > d:
        count += 1
print(count)
