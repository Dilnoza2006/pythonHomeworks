def remove_by_index(lst, index):
    if 0 <= index < len(lst):
        return lst[:index] + lst[index+1:]
    return lst  
print(remove_by_index([1, 2, 3, 4], 2))