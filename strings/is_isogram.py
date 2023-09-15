# isogram -> repeated letters

def is_isogram(string: str) -> bool:
    if not all(x.isalpha() for x in string):
        raise ValueError("String must only contain alphabetic characters.")

    letters = sorted(string.lower())
    return len(letters) == len(set(letters))

print(is_isogram('Uncopyrightable'))
# >>> True
print(is_isogram('allowance'))
# >>> False