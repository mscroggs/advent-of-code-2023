def get_value(card):
    if card == "A":
        return 13
    if card == "K":
        return 12
    if card == "Q":
        return 11
    if card == "T":
        return 10
    if card == "J":
        return 1
    return int(card)


def score(hand):
    out = 0
    for i in hand:
        out *= 14
        out += get_value(i)
    return out


def get_counts(hand):
    if len(hand) == 0:
        return []
    return sorted([hand.count(hand[0])] + get_counts("".join(i for i in hand if i != hand[0])))[::-1]


def get_counts_jokers(hand):
    jokers = hand.count("J")
    c = get_counts("".join(i for i in hand if i != "J"))
    if len(c) == 0:
        c.append(0)
    return [c[0] + jokers] + c[1:]


def rate_hand(hand):
    counts = get_counts_jokers(hand)
    if counts[0] == 5:
        return 6*14**5 + score(hand)
    if counts[0] == 4:
        return 5*14**5 + score(hand)
    if counts[0] == 3 and counts[1] == 2:
        return 4*14**5 + score(hand)
    if counts[0] == 3:
        return 3*14**5 + score(hand)
    if counts[0] == 2 and counts[1] == 2:
        return 2*14**5 + score(hand)
    if counts[0] == 2:
        return 14**5 + score(hand)
    return score(hand)


hands = []
with open("input") as f:
    for line in f:
        hand, value = line.strip().split()
        value = int(value)
        hands.append((hand, value))

hands.sort(key=lambda i: rate_hand(i[0]))

print(sum((i + 1) * j[1] for i, j in enumerate(hands)))
