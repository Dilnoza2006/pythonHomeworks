def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Example
d = {'a': 3, 'b': 1, 'c': 2}
print(sort_dict_by_value(d)) 