def invert_dictionary(d):
    return {v: k for k, v in d.items()}

print(invert_dictionary({"a": 1, "b": 2}))