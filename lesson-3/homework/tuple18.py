def min_of_subtuple(tpl, start, end):
    return min(tpl[start:end]) if start < end else None

print(min_of_subtuple((1, 5, 3, 9, 2), 1, 4)) 