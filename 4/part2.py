total = 0
count = {1: 1}
with open("input") as f:
    for line in f:
        card_n, rest = line.strip().split(": ")
        card_n = int(card_n.split(" ")[-1])
        winning, numbers = rest.split(" | ")
        winning = [int(i) for i in winning.split(" ") if i != ""]
        numbers = [int(i) for i in numbers.split(" ") if i != ""]

        if card_n not in count:
            count[card_n] = 1
        n = len([i for i in winning if i in numbers])
        for i in range(1, n+1):
            if card_n + i not in count:
                count[card_n + i] = 1
            count[card_n + i] += count[card_n]
print(sum(count.values()))
