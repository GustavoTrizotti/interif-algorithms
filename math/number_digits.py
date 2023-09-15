import math

def num_digits(n: int) -> int:
    return len(str(abs(n)))

print(num_digits(2356423322546436212335532))
# >>> 25