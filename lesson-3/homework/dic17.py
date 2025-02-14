def get_nested_value(d, keys):
    for key in keys:
        d = d.get(key, {})
    return d if d else None

# Example
nested_dict = {'a': {'b': {'c': 42}}}
print(get_nested_value(nested_dict, ['a', 'b', 'c']))