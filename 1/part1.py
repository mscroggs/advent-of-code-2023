total = 0
with open("input") as f:
    for line in f:
        digits = [i for i in line.strip() if i in "0123456789"]
        total += int(f"{digits[0]}{digits[-1]}")
print(total)
