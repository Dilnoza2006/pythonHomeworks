def find_sublist(lst, sublist):
    n, m = len(lst), len(sublist)
    for i in range(n - m + 1):
        if lst[i:i + m] == sublist:
            return True
    return False
print(find_sublist([1, 2, 3, 4, 5], [3, 4]))  # Output: True
print(find_sublist([1, 2, 3], [4, 5]))