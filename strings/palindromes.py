def is_palindrome(s: str) -> bool:
    start_i = 0
    end_i = len(s) - 1
    while start_i < end_i:
        if s[start_i] == s[end_i]:
            start_i += 1
            end_i -= 1
        else:
            return False
    return True

def is_palindrome_recursive(s: str) -> bool:
    if len(s) <= 2:
        return True
    if s[0] == s[len(s) - 1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        return False
    
def is_palindrome_slice(s: str) -> bool:
    return s == s[::-1]

print(is_palindrome("amanaplanacanalpanama"))
# >>> True
print(is_palindrome("teste"))
# >>> False