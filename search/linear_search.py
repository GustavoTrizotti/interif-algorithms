def linear_search(sequence: list, target: int) -> int:
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return -1

def rec_linear_search(sequence: list, low: int, high: int, target: int) -> int:
    if not (0 <= high < len(sequence) and 0 <= low < len(sequence)):
        raise Exception("Invalid upper or lower bound!")
    if high < low:
        return -1
    if sequence[low] == target:
        return low
    if sequence[high] == target:
        return high
    return rec_linear_search(sequence, low + 1, high - 1, target)

print(linear_search([0, 30, 500, 100, 700], 30))
# >>> 1
print(rec_linear_search([0, 30, 500, 100, 700], 0, 4, 100))
# >>> 4