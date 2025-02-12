def create_nested_tuple(tpl, size):
    return tuple(tpl[i:i+size] for i in range(0, len(tpl), size))

print(create_nested_tuple((1, 2, 3, 4, 5, 6), 2))  