def rotate_list(lst, k):
    k %= len(lst) 
    return lst[-k:] + lst[:-k] if lst else lst
print(rotate_list([1, 2, 3, 4, 5], 2)) 