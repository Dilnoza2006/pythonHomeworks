def min_element(lst):
    if not lst:
        return None  # Return None if the list is empty
    return min(lst)

# Example usage:
numbers = [13,15,12,141,5,-2]
print(min_element(numbers))