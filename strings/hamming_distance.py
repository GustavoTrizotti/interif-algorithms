def hamming_distance(string1: str, string2: str) -> int:
    if len(string1) != len(string2):
        raise ValueError("String lengths must match!")

    count = 0

    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            count += 1

    return count

print(hamming_distance("karolin", "kathrin"))
# >>> 3
print(hamming_distance("peter", "peterson"))
# >>> ValueError: String lengths must match!