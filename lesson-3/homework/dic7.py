def remove_key(d, key):
    d.pop(key, None)  

d = {"a": 1, "b": 2}
remove_key(d, "a")
print(d) 