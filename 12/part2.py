from itertools import combinations

cache = {}

def count_correct(data, ns):
    global cache
    if "?" in data:
        if (data, ns) in cache:
            return cache[(data, ns)]

        end, rem = data.split("?", 1)
        rem = "?" + rem

        while end.endswith("#"):
            end = end[:-1]
            rem = "#" + rem
        start = tuple(len(i) for i in end.split(".") if i != "")
        if start != ns[:len(start)]:
            cache[(data, ns)] = 0
            return 0

        ns_rem = ns[len(start):]
        if sum(ns_rem) + len(ns_rem) - 1 > len(rem):
            cache[(data, ns)] = 0
            return 0

        count = 0
        for c in ".#":
            count += count_correct(rem.replace("?", c, 1), ns_rem)
        cache[(data, ns)] = count
        return count

    else:
        if tuple(len(i) for i in data.split(".") if i != "") == ns:
            return 1
        return 0



options = 0
with open("input") as f:
    for line in f:
        data, ns = line.strip().split()
        data = "?".join([data for _ in range(5)])
        ns = tuple(int(i) for _ in range(5) for i in ns.split(","))

        options += count_correct(data, ns)
print(options)
