total = 0

with open("input") as f:
    for line in f:
        id = int(line.split("Game ")[1].split(": ")[0])
        r = 0
        g = 0
        b = 0
        for show in line.strip().split(": ")[1].split("; "):
            cubes = {i.split(" ")[1]: int(i.split(" ")[0])
                     for i in show.split(", ")}
            if "red" in cubes:
                r = max(r, cubes["red"])
            if "green" in cubes:
                g = max(g, cubes["green"])
            if "blue" in cubes:
                b = max(b, cubes["blue"])
        total += r * g * b

print(total)
