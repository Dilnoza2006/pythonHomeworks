def max_element(lst):
    if not lst:
        return None  
    return max(lst)
numbers = [12,15,21,14,15,141,175,201]
print(max_element(numbers))