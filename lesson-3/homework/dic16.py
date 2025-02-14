def has_nested_dict(d):
    return any(isinstance(v, dict) for v in d.values())

d = {'a': 1, 'b': {'c': 2}}
print(has_nested_dict(d))