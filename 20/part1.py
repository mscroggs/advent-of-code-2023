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


def fire(status):
    pulses = [(i, "low", "broadcaster") for i in broadcaster]
    nlow = len(broadcaster) + 1
    nhigh = 0
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
                                nhigh += 1
                                np.append((t, "high", i))
                        else:
                            assert status[i] == "on"
                            status[i] = "off"
                            for t in targets:
                                nlow += 1
                                np.append((t, "low", i))
                else:
                    assert mtype == "&"
                    status[i][source] = p
                    if "low" in list(status[i].values()):
                        for t in targets:
                            nhigh += 1
                            np.append((t, "high", i))
                    else:
                        for t in targets:
                            nlow += 1
                            np.append((t, "low", i))
        pulses = np
    return status, nlow, nhigh


status = {}
for mid, (mtype, _) in modules.items():
    if mtype == "%":
        status[mid] = "off"
    else:
        status[mid] = {i: "low" for i, (_, targets) in modules.items() if mid in targets}
        if mid in broadcaster:
            status[mid]["broadcaster"] = "low"

ltotal = 0
htotal = 0
for _ in range(1000):
    status, nlow, nhigh = fire(status)
    ltotal += nlow
    htotal += nhigh

print(ltotal * htotal)
