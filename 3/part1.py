with open("input") as f:
    engine = [[i for i in line.strip()] for line in f]

def next_to_symbol(i, j, n):
    info = ""
    for a, b in [
        (k, l) for k in [i-1, i+n] for l in [j-1, j, j+1]
    ] + [
        (k, l) for k in range(i, i+n) for l in [j-1, j+1]
    ]:
        if 0 <= b < len(engine) and 0 <= a < len(engine[b]):
            info += engine[b][a]
    for a, b in [
        (k, l) for k in [i-1, i+n] for l in [j-1, j, j+1]
    ] + [
        (k, l) for k in range(i, i+n) for l in [j-1, j+1]
    ]:
        if 0 <= b < len(engine) and 0 <= a < len(engine[b]):
            if engine[b][a] not in "0123456789.":
                return True
    return False

total = 0
n = ""
for j, row in enumerate(engine):
    for i, item in enumerate(row + ["."]):
        if item in "0123456789":
            n += item
        else:
            if n != "":
                if next_to_symbol(i - len(n), j, len(n)):
                    total += int(n)
            n = ""
print(total)
