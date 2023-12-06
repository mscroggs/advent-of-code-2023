with open("input") as f:
    times, distances = f.read().strip().split("\n")
    times = [int(i) for i in times.split()[1:]]
    distances = [int(i) for i in distances.split()[1:]]

result = 1
for t, d in zip(times, distances):
    count = 0
    for hold in range(t + 1):
        distance = hold * (t - hold)
        if distance > d:
            count += 1
    result *= count
print(result)
