def count_value_occurrences(d, value):
    return list(d.values()).count(value)

print(count_value_occurrences({"a": 1, "b": 2, "c": 1}, 1)) 