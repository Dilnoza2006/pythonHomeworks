def is_sorted(tpl):
    return tpl == tuple(sorted(tpl))

print(is_sorted((1, 2, 3, 4)))  
print(is_sorted((3, 1, 4, 2)))