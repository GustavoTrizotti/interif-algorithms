import random

def bogo_sort(collection):
    def is_sorted(collection):
        for i in range(len(collection) -1):
            if collection[i] > collection[i+1]:
                return False
        return True
    
    while not is_sorted(collection):
        random.shuffle(collection)
    return collection

print(bogo_sort([0, 5, 3, 2, 2]))
# >>> [0, 2, 2, 3, 5]