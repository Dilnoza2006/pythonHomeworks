def is_palindrome(tpl):
    return tpl == tpl[::-1]

print(is_palindrome((1, 2, 3, 2, 1))) 
print(is_palindrome((1, 2, 3, 4))) 