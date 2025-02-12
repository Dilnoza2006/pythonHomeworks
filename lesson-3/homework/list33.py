def find_all_indices(lst, element):
    return [i for i, val in enumerate(lst) if val == element]
print(find_all_indices([1, 2, 3, 2, 4, 2], 2))