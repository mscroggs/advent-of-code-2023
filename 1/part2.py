total = 0
digits = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9
}
for i in "0123456789":
    digits[i] = int(i)

with open("input") as f:
    for line in f:
        line = line.strip()
        first = ""
        while True:
            for d, v in digits.items():
                if line.startswith(d):
                    first = v
                    break
            else:
                line = line[1:]
                continue
            break
        last = ""
        while True:
            for d, v in digits.items():
                if line.endswith(d):
                    last = v
                    break
            else:
                line = line[:-1]
                continue
            break
        total += int(f"{first}{last}")
print(total)
