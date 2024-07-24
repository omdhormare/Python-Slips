s = (10, 20, 30, 40, 10, 20, 30)

def find_repeats(t):
    repeats = []
    for item in t:
        if t.count(item) > 1 and item not in repeats:
            repeats.append(item)
    return repeats

print(find_repeats(s))
