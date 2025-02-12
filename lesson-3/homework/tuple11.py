def get_all_indices(tpl, element):
    return [i for i, val in enumerate(tpl) if val == element]

print(get_all_indices((1, 2, 3, 2, 4, 2), 2))