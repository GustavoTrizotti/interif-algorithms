def reverse_words(input_str: str) -> str:
    return " ".join(input_str.split()[::-1])

print(reverse_words('Texto exemplo.'))
# >>> exemplo. Texto
