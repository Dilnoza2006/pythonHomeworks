def replace_element(lst, old, new):
    if old in lst:
        index = lst.index(old)
        lst[index] = new  
    return lst
print(replace_element([1, 2, 3, 2], 2, 10)) 