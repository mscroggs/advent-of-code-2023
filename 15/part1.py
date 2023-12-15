with open("input") as f:
    strs = f.read().strip().split(",")

total = 0
for s in strs:
    n = 0
    for c in s:
        n += ord(c)
        n *= 17
        n %= 256
    total += n
print(total)
