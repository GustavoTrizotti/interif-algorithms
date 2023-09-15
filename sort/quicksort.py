import random

# worstCase - o(n^2)
# bestCase - o(nlogn)
# defaultCase - o(nlogn)

def quick_sort(collection):
    if len(collection) < 2:
        return collection
    pivot_index = random.randrange(len(collection))
    pivot = collection[pivot_index]
    greater: list[int] = []
    lesser: list[int] = []

    for element in collection[:pivot_index]:
        (greater if element > pivot else lesser).append(element)

    for element in collection[pivot_index + 1:]:
        (greater if element > pivot else lesser).append(element)

    return [*quick_sort(lesser), pivot, *quick_sort(greater)]

print(quick_sort([2, 5, 1, 10, 9]))
# >>> [1, 2, 5, 9, 10]