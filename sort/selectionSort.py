def selection_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i+1, length):
            if collection[k] < collection[least]:
                least = k
        if least != i:
            collection[least], collection[i] = (collection[i], collection[least])
    return collection

print(selection_sort([2, 5, 1, 10, 9]))
# >>> [1, 2, 5, 9, 10]