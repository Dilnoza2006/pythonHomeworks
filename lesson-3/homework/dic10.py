def get_key_value_pair(d, key):
    return (key, d[key]) if key in d else None

print(get_key_value_pair({"a": 1, "b": 2}, "a"))  
print(get_key_value_pair({"a": 1, "b": 2}, "c")) 