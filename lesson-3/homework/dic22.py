def filter_by_value(d, condition):
    return {k: v for k, v in d.items() if condition(v)}

# Example
d = {'a': 1, 'b': 10, 'c': 20}
print(filter_by_value(d, lambda v: v > 5))