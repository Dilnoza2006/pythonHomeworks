def check_key(d, key):
    return key in d

print(check_key({"a": 1, "b": 2}, "a"))  
print(check_key({"a": 1, "b": 2}, "c")) 