def median(nums: list) -> int | float:
    sorted_list = sorted(nums)
    length = len(sorted_list)
    mid_index = length >> 1
    return (
        (sorted_list[mid_index] + sorted_list[mid_index - 1]) / 2
        if length % 2 == 0
        else sorted_list[mid_index]
    )

print(median([2, 70, 6, 50, 20, 8, 4]))

# >>> 8