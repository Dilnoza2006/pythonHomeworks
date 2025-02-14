def get_first_key_value(d):
    return next(iter(d.items()), None)

# Example
d = {'x': 100, 'y': 200}
print(get_first_key_value(d))