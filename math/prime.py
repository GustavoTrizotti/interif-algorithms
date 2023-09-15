import math

def is_prime(number: int) -> bool:
    if 1 < number < 4:
        return True
    elif number < 2 or not number % 2:
        return False

    odd_numbers = range(3, int(math.sqrt(number) + 1), 2)
    return not any(not number % i for i in odd_numbers)

print(is_prime(23))
# >>> True