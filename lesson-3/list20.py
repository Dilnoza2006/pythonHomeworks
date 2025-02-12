def second_largest(lst):
    unique_lst = list(set(lst)) 
    if len(unique_lst) < 2:
        return None 
    unique_lst.sort(reverse=True)
    return unique_lst[1]  
print(second_largest([4, 1, 7, 7, 3, 6])) 