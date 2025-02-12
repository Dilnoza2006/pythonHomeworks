def get_value(d, key, default=None):
    return d.get(key, default)

print(get_value({"a": 1, "b": 2}, "a"))  # Output: 1
print(get_value({"a": 1, "b": 2}, "c", "Not found"))