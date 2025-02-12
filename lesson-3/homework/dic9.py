def is_dict_empty(d):
    return not bool(d)

print(is_dict_empty({}))  
print(is_dict_empty({"a": 1}))