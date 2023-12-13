with open("input") as f:
    patterns = [[[j for j in i] for i in p.split("\n") if i != ""]
                for p in f.read().split("\n\n")]

result = 0
for p in patterns:
    for i in range(1, len(p)):
        l = min(i, len(p) - i)
        if p[i - l:i] == p[i:i + l][::-1]:
            result += 100 * i
            break
    else:
        for i in range(1, len(p[0])):
            l = min(i, len(p[0]) - i)
            if [j[i - l:i] for j in p] == [j[i:i + l][::-1] for j in p]:
                result += i
                break
        else:
            raise ValueError()
print(result)
