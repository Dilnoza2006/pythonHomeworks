def get_middle(lst):
    n = len(lst)
    if n == 0:
        return None
    mid = n // 2
    return lst[mid] if n % 2 != 0 else [lst[mid - 1], lst[mid]]
print(get_middle([1, 2, 3, 4, 5])) 
print(get_middle([1, 2, 3, 4]))