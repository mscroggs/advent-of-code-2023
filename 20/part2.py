modules = {}
broadcaster = None
with open("input") as f:
    for line in f:
        if line.startswith("broadcaster"):
            broadcaster = line.split(" -> ")[1].strip().split(", ")
        else:
            mtype = line[0]
            mid = line[1:].split(" ")[0]
            targets = line.split(" -> ")[1].strip().split(", ")
            modules[mid] = (mtype, targets)

# low to rx
# high to hj
assert [m[0] for m in modules.items() if "rx" in m[1][1]] == ["hj"]
# low to pre
pre = [m[0] for m in modules.items() if "hj" in m[1][1]]
# high to prepre
prepre = [m[0] for m in modules.items() if "ks" in m[1][1] or "jf" in m[1][1] or "qs" in m[1][1] or "zk" in m[1][1]]


def fire(status):
    pulses = [(i, "low", "broadcaster") for i in broadcaster]
    low = []
    while len(pulses) > 0:
        np = []
        for i, p, source in pulses:
            if i in modules:
                mtype, targets = modules[i]
                if mtype == "%":
                    if p == "low":
                        if status[i] == "off":
                            status[i] = "on"
                            for t in targets:
                                np.append((t, "high", i))
                        else:
                            assert status[i] == "on"
                            status[i] = "off"
                            for t in targets:
                                np.append((t, "low", i))
                else:
                    assert mtype == "&"
                    status[i][source] = p
                    if "low" in list(status[i].values()):
                        for t in targets:
                            np.append((t, "high", i))
                    else:
                        for t in targets:
                            np.append((t, "low", i))

            if i in prepre and p == "high":
                if "low" not in list(status[i].values()):
                    low.append(i)
        pulses = np
    return status, low

status = {}
for mid, (mtype, _) in modules.items():
    if mtype == "%":
        status[mid] = "off"
    else:
        status[mid] = {i: "low" for i, (_, targets) in modules.items() if mid in targets}
        if mid in broadcaster:
            status[mid]["broadcaster"] = "low"


pings = {i: [] for i in prepre}

for i in range(10000):
    status, info = fire(status)
    if len(info) > 0:
        for j in info:
            pings[j].append(i)

n = 1
for p in pings.values():
    n *= p[0] + 1

print(n)
