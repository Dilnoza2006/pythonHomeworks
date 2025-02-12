def max_of_sublist(lst, start, end):
    return max(lst[start:end]) if start < end and end <= len(lst) else None
print(max_of_sublist([1, 5, 3, 9, 2], 1, 4)) 