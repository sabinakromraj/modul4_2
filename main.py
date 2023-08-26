def is_palindrome(word):
    """
        The function compares the original word with its reversed version. 
        If they are identical, returns True. 
        Otherwise, returns False.
    """
    reversed_word = word[::-1]
    return word == reversed_word

print(is_palindrome("kajak"))
print(is_palindrome("potop")) 
print(is_palindrome("laptop"))
