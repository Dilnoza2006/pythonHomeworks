def second_smallest(lst):
    unique_lst = list(set(lst))
    if len(unique_lst) < 2:
        return None
    unique_lst.sort()
    return unique_lst[1]

print(second_smallest([4, 1, 7, 7, 3, 6]))