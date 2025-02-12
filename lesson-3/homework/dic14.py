def find_keys_with_value(d, value):
    return [k for k, v in d.items() if v == value]

print(find_keys_with_value({"a": 1, "b": 2, "c": 1}, 1))