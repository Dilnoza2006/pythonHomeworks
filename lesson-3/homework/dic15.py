def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(create_dict_from_lists(keys, values))  