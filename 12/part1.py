from itertools import product

def counts(row):
    return tuple(len(i) for i in row.split(".") if i != "")

options = 0
with open("input") as f:
    for line in f:
        data, ns = line.strip().split()
        ns = tuple(int(i) for i in ns.split(","))

        unknown = data.count("?")

        for chars in product(".#", repeat=unknown):
            row = data + ""
            for i in chars:
                row = row.replace("?", i, 1)
            if counts(row) == ns:
                print(row, ns)
                options += 1
print(options)
