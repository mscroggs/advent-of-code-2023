total = 0
with open("input") as f:
    for line in f:
        winning, numbers = line.strip().split(": ")[1].split(" | ")
        winning = [int(i) for i in winning.split(" ") if i != ""]
        numbers = [int(i) for i in numbers.split(" ") if i != ""]

        n = len([i for i in winning if i in numbers])
        if n > 0:
            total += 2 ** (n - 1)
print(total)
