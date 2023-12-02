total = 0

with open("input") as f:
    for line in f:
        id = int(line.split("Game ")[1].split(": ")[0])
        for show in line.strip().split(": ")[1].split("; "):
            cubes = {i.split(" ")[1]: int(i.split(" ")[0])
                     for i in show.split(", ")}
            if "red" in cubes and cubes["red"] > 12:
                break
            if "green" in cubes and cubes["green"] > 13:
                break
            if "blue" in cubes and cubes["blue"] > 14:
                break
        else:
            total += id

print(total)
