def check_common_keys(d1, d2):
    return bool(set(d1.keys()) & set(d2.keys()))

# Example
d1 = {'x': 10, 'y': 20}
d2 = {'y': 5, 'z': 15}
print(check_common_keys(d1, d2))